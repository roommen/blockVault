import os
import datetime
import socket
fileName = ""

def downloadCoreLogic(fileName):
    # print("Download core logic")
    downloadAWS(fileName)
    downloadGCP(fileName)
    joinSplits(fileName)
    cleanupDownloadSplits(fileName)
    makeDownloadMetaData(fileName)

def downloadAWS(fileName):
    # print("Download AWS functionality")
    # global fileName
    print("\nDownloading file chunk from AWS S3...")
    cmd = "aws s3 cp s3://inouthack6/" + fileName + "aa" + " /tmp/"
    # print("cmd is", cmd)
    os.system(cmd)
    # print("Upload to AWS S3 complete")

def downloadGCP(fileName):
    # print("Download GCP functionality")
    # global fileName
    print("\nDownloading file chunk from GCP CloudStorage...")
    cmd = "gsutil cp gs://inouthack6/" + fileName + "ab" + " /tmp/"
    # print("cmd is", cmd)
    os.system(cmd)
    # print("Upload to AWS S3 complete")

def joinSplits(fileName):
    # print("Join file functionality")
    cmd = "cat /tmp/" + fileName + "a* > /tmp/" + fileName
    os.system(cmd)
    msg = "\nFile downloaded successfully - /tmp/" + fileName
    print(msg)

def cleanupDownloadSplits(fileName):
    # print("cleanup functionality")
    cmd = "rm -rf /tmp/" + fileName + "a*"
    os.system(cmd)

def makeDownloadMetaData(fileName):
    action = "download"

    timestamp = datetime.datetime.now()

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ipAddress = s.getsockname()[0]
    s.close()

    print(fileName, action, timestamp, ipAddress)

def uploadCoreLogic(filePath):
    getFileName(filePath)
    splitFile(filePath)
    uploadAWS()
    uploadGCP()
    cleanupUploadSplits()
    makeUploadMetaData()

def getFileName(filePath):
    global fileName
    fileName = os.path.basename(filePath)

def splitFile(filePath):
    global fileName
    # print("Split file functionality")
    # print("file path is", filePath)
    cmd = "split -n 2 " + filePath + " /tmp/" + fileName
    # print("cmd is", cmd)
    os.system(cmd)

def uploadAWS():
    global fileName
    print("\nUploading file chunk to AWS S3...")
    cmd = "aws s3 cp /tmp/" + fileName + "aa" + " s3://inouthack6"
    # print("cmd is", cmd)
    os.system(cmd)
    # print("Upload to AWS S3 complete")

def uploadGCP():
    global fileName
    print("\nUploading file chunk to GCP CloudStorage...")
    cmd = "gsutil cp /tmp/" + fileName + "ab" + " gs://inouthack6"
    # print("cmd is", cmd)
    os.system(cmd)
    # print("Upload to GCP complete")

def cleanupUploadSplits():
    global fileName
    # print("cleanup functionality")
    cmd = "rm -rf /tmp/" + fileName + "a*"
    os.system(cmd)

def makeUploadMetaData():
    global fileName

    action = "upload"

    timestamp = datetime.datetime.now()

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ipAddress = s.getsockname()[0]
    s.close()

    print(fileName, action, timestamp, ipAddress)
