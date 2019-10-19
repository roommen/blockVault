import os

def splitFile(filePath):
    # print("Split file functionality")
    # print("file path is", filePath)
    fileName = os.path.basename(filePath)
    cmd = "split -n 2 " + filePath + " /tmp/" + fileName
    # print("cmd is", cmd)
    os.system(cmd)

def uploadAWS():
    print("Upload to AWS S3 functionality")

def uploadGCP():
    print("Upload to GCP CloudBucket functionality")

def joinFile():
    print("Join file functionality")
