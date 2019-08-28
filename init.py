import json
from PyInquirer import prompt
import re
import helper

def selectProject():
    projectsList = json.loads(helper.execCmd("gcloud projects list --format 'json'"))
    projectsNameList = map(lambda item: item["name"], projectsList)
    questions = [
        {
            'type': 'list',
            'name': 'name',
            'message': 'Please select your project',
            'choices': projectsNameList
        }
    ]
    answers = prompt(questions)
    projectsAnsId = list(filter(lambda item: item["name"] == answers["name"], projectsList))[0]["projectId"]
    helper.execCmd( "gcloud config set project {}".format(projectsAnsId))

def checkRule():
    rulesList = json.loads(helper.execCmd("gcloud compute firewall-rules list --format=json"))
    if list(filter(lambda item: item["name"] == "gaming-instance", rulesList)) == []:
        helper.execCmd("""
gcloud compute firewall-rules create gaming-instance \
    --direction=INGRESS \
    --priority=1000 \
    --network=default \
    --action=ALLOW \
    --rules=all \
    --source-ranges=0.0.0.0/0 \
    --target-tags=gaming-instance
""")

def createInstance():
    answers = dict()

    countryQuestions = [
        {
            'type': 'list',
            'name': 'country',
            'message': 'Please select your country',
            'choices': [
                "Taiwan",
                "Japan",
                "Singapore"
            ]
        }
    ]
    answers.update(prompt(countryQuestions))

    if answers["country"] == "Taiwan":
        choices = [
            "asia-east1-a/nvidia-tesla-p100",
            "asia-east1-c/nvidia-tesla-p100",
            "asia-east1-c/nvidia-tesla-v100"
        ]
    elif answers["country"] == "Japan":
        choices = [
            "asia-northeast1-a/nvidia-tesla-t4"
        ]
    elif answers["country"] == "Singapore":
        choices = [
            "asia-southeast1-b/nvidia-tesla-p4",
            "asia-southeast1-b/nvidia-tesla-p100",
            "asia-southeast1-c/nvidia-tesla-v100"
        ]
    gpuQuestions = [
        {
            'type': 'list',
            'name': 'gpu',
            'message': 'Please select your GPU',
            'choices': choices
        }
    ]
    gpuAnswers = re.search("(.+)/(.+)", prompt(gpuQuestions)["gpu"])
    answers["zone"] = gpuAnswers.group(1)
    answers["gpu"] = gpuAnswers.group(2)

    helper.execCmd("""
gcloud compute instances create gaming-instance \
    --zone={} \
    --machine-type=n1-standard-4 \
    --maintenance-policy=TERMINATE \
    --accelerator=type={},count=1 \
    --tags=gaming-instance,http-server,https-server \
    --image=windows-server-2016-dc-v20190709 \
    --image-project=windows-cloud \
    --boot-disk-size=150GB \
    --boot-disk-type=pd-ssd \
    --preemptible \
    --no-boot-disk-auto-delete \
    --metadata-from-file windows-startup-script-ps1=install_check.ps1
""".format(answers["zone"], answers["gpu"]))

if __name__ == '__main__':
    selectProject()
    checkRule()
    createInstance()