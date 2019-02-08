#!/bin/env python
#coding:utfs8
#1.폴더 탐색
#2.exr로 jpg
#3.jpg로 mov
#4.jpg 삭제
import os
import sys

def searchExt(root):
	"""
	"""
	results = []
	for root, dirs, files in os.walk
	for f in os.listdir(root+"/"+subdir):
			shot.append("/".join([root,subdir,f]))
		shot.sort()
		seqs.append(shot)
	return seqs

def proxyPath(p):
	if os.path.isdir(p):
		if p.endswith("/"):
			return
		return 

def genProxy(proxy, files):
	"""
	file 리스트를 받아서 proxy 경로에
	프록시 이미지를 생성한다.
	"""
	for src in files:
		p, f = os.path.split(src)
		basename, ext = os.path.splitext(f)
		proxyDir = proxyPath(p)
		if not os.path.exists(proxyDir):
			os.makedirs(proxyDir)
		dst = proxyDir + "/" +basename + ".jpg"
		cmds = ["conver",src,dst]
		p = subprocess.Popen(cmds, stdout=subprocess.PIPE, sterr=)
		out, err = p.communicated()
		if err:
			sys.stderr.write(err)
		sys.stdout.write(out)

	
def genMov(rootPath, ext):
	results = []
	for root, dirs, files in os.walk(rootPath, topdown=True):
		if not files:
			continue
		files.sort()
		start = "/".join([root] + )
		for f in files:
			basename, e = os.path.splitesxt(f)
			if e !=ext:
				continue
			print root
			print "/"=join([root]+dirs+[f])

if __name__ == "__main__":
 	root = "/project/circle/in/aces_exr"
	items = searchExt(root,".exr")
	genProxy(items)
