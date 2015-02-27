# -*- coding: utf-8 -*-
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element
import os
import time
from phoneweb.com.common import const
import logging

__author__ = 'guojing'

XMLFile = os.getcwdu() + "/xml/phone.xml"

logger = logging.getLogger("gj")

def read_xml():
    logger.info("rrrrrrrrrrrrrr")
    if not os.path.exists(XMLFile):
        fo = open(XMLFile,"w")
        fo.write("<?xml version='1.0' encoding='utf-8'?><users></users>")
        fo.close()

    root = ET.parse(XMLFile).getroot()
    users = root.findall('user')
    userArr = []
    for user in users:
        id = user.find(const.ContactConst.CONTACT_ID).text
        name = user.find(const.ContactConst.CONTACT_NAME).text
        tele = user.find(const.ContactConst.CONTACT_TELE).text
        userInfo = {
            const.ContactConst.CONTACT_ID: id,
            const.ContactConst.CONTACT_NAME: name,
            const.ContactConst.CONTACT_TELE: tele
        }
        userArr.append(userInfo)
    return userArr

def insert(name, telephone):
    tree = ET.parse(XMLFile)
    root = tree.getroot()
    user = Element("user")
    root.append(user)

    idNode = Element("id")
    idNode.text = generateID()
    user.append(idNode)

    nameNode = Element("name")
    nameNode.text = name
    user.append(nameNode)

    phoneNode = Element("telephone")
    phoneNode.text = telephone
    user.append(phoneNode)
    try:
        tree.write(XMLFile, encoding="utf-8", xml_declaration=True)
        return 1
    except Exception as e:
        print e
        return 0


def update(id, name, telephone):
    tree = ET.parse(XMLFile)
    root = tree.getroot()
    users = root.findall('user')  # 找到所有user节点
    for user in users:
        if user.find("id").text == id:
            teleNode = user.find("telephone")
            teleNode.text = telephone
            nameNode =  user.find("name")
            nameNode.text = name
    try:
        tree.write(XMLFile, encoding="utf-8", xml_declaration=True)
        return 1
    except Exception as e:
        print e
        return 0


def delete(id):
    tree = ET.parse(XMLFile)
    root = tree.getroot()
    users = root.findall('user')  # 找到所有user节点
    for user in users:
        if user.find("id").text == id:
            user.remove(user.find("id"))
            user.remove(user.find("name"))
            user.remove(user.find("telephone"))
            user.clear()
            root.remove(user)
    try:
        tree.write(XMLFile, encoding="utf-8", xml_declaration=True)
        return 1;
    except Exception as e:
        print e
        return 0;


def generateID():
    return time.strftime('%Y%m%d_%H%M%S')


if __name__ == '__main__':
    # tree = update()

    #write_xml(tree,"D:\\phone.xml")
    # read_xml()
    userInfo = findUser("ddd")
    print userInfo