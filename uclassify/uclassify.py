#!/usr/bin/python3

from xml.dom.minidom import Document
from time import gmtime, strftime
from uclassify_eh import uClassifyError
import xml.dom.minidom
import requests

class uclassify:
    def __init__(self):
        self.api_url = "http://api.uclassify.com"
        self.writeApiKey=None
        self.readApiKey=None

    def setWriteApiKey(self,key):
        self.writeApiKey = key

    def setReadApiKey(self,key):
        self.readApiKey = key

    def _buildbasicXMLdoc(self):
        doc = Document()
        root_element = doc.createElementNS('http://api.uclassify.com/1/RequestSchema', 'uclassify')
        root_element.setAttribute("version", "1.01")
        root_element.setAttribute("xmlns", "http://api.uclassify.com/1/RequestSchema")
        doc.appendChild(root_element)
        #texts = doc.createElement("texts")
        #root_element.appendChild(texts)
        #print(doc.toprettyxml())
        return doc,root_element

    def _getText(self,nodelist):
        rc = []
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc.append(node.data)
        return ''.join(rc)

    def _getResponseCode(self,content):
        """Returns the status code from the content.
           :param content: (required) XML Response content
        """
        doc = xml.dom.minidom.parseString(content)
        node = doc.documentElement
        status = node.getElementsByTagName("status")
        success = status[0].getAttribute("success")
        status_code = status[0].getAttribute("statusCode")
        text = self._getText(status[0].childNodes)
        return success, status_code, text

    def create(self,classifierName):
        """Creates a new classifier.
           :param classifierName: (required) The Classifier Name you are going to create.
        """
        doc,root_element = self._buildbasicXMLdoc()
        writecalls = doc.createElement("writeCalls")
        writecalls.setAttribute("writeApiKey",self.writeApiKey) #Add exception handling here
        writecalls.setAttribute("classifierName",classifierName)
        create = doc.createElement("create")
        cur_time = strftime("%Y%m%d%H%M", gmtime())
        create.setAttribute("id",cur_time + "create" + classifierName)
        root_element.appendChild(writecalls)
        writecalls.appendChild(create)
        r = requests.post(self.api_url,doc.toxml())
        if r.status_code == 200:
            success, status_code, text = self._getResponseCode(r.content)
            if success == "false":
                raise uClassifyError(text,status_code)
        else:
            raise uClassifyError("Bad XML Request Sent")

    def addClass(self,className,classifierName):
        """Adds class to an existing Classifier.
           :param className: (required) A List containing various classes that has to be added for the given Classifier.
           :param classifierName: (required) Classifier where the classes will be added to.
        """
        
        
if __name__ == "__main__":
    a = uclassify()
    a.setWriteApiKey("fsqAft7Hs29BgAc1AWeCIWdGnY")
    a.create("ManorWoma")
