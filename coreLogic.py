import os

def splitFile(filePath):
    # print("Split file functionality")
    # print("file path is", filePath)
    fileName = os.path.basename(filePath)
    cmd = "split -n 2 " + filePath + " /tmp/" + fileName
    # print("cmd is", cmd)
    os.system(cmd)
    uploadAWS(fileName)
    uploadGCP(fileName)
    cleanupSplits()

def uploadAWS(fileName):
    print("Uploading file chunk to AWS S3...")
    cmd = "aws s3 cp /tmp/" + fileName + "aa" + " s3://inouthack6"
    # print("cmd is", cmd)
    os.system(cmd)
    # print("Upload to AWS S3 complete")

def uploadGCP(fileName):
    print("Uploading file chunk to GCP CloudStorage...")
    cmd = "gsutil cp /tmp/" + fileName + "ab" + " gs://inouthack6"
    # print("cmd is", cmd)
    os.system(cmd)
    # print("Upload to GCP complete")

def cleanupSplits():
    print("cleanup functionality")

def joinFile():
    print("Join file functionality")
