from tkinter import Tk,Frame,Button
import os
import subprocess

def GitHubScript():
	pid = os.fork()
	if pid==0:
		print("GITHUB")
		os.system("qterminal -e 'bash gitAuto.sh'")
	if pid>0:
		os.waitpid(pid,0)

def Sudoku():
	pid = os.fork()
	if pid==0:
		print("SUDOKU")
		os.system("qterminal -e './sudoku'")
	if pid>0:
		os.waitpid(pid,0)


def Deadlock():
	pid = os.fork()
	if pid==0:
		print("DEADLOCK")
		os.system("qterminal -e 'python3 rag.py'")
	if pid>0:
		os.waitpid(pid,0)

def Dining():
	pid = os.fork()
	if pid==0:
		print("Dining Philosopher")
		os.system("qterminal -e 'python3 dining.py'")
	if pid>0:
		os.waitpid(pid,0)

def ShowDialogs(method):
	if method==1:
		GitHubScript()
	if method == 2:
		Sudoku()
	if method == 3:
		Deadlock()
	if method==4:
		Dining()


window=Tk()
window.title("Multi - Purpose Utility Hub")

frame=Frame(window,bg="#1B2631")
frame.pack(fill="both",expand=True)

button1=Button(frame,text="GitHub Automation Script",padx=10,pady=10,bg="#C0392B",fg="white",command=lambda:ShowDialogs(1))
button1.grid(row=0,column=0,sticky="nsew",padx=10,pady=10)

button2=Button(frame,text="Multi-Threaded Sudoku Solver",padx=10,pady=10,bg="#C0392B",fg="white",command=lambda:ShowDialogs(2))
button2.grid(row=0,column=1,sticky="nsew",padx=10,pady=10)

button3=Button(frame,text="Deadlock Detection with RAG",padx=10,pady=10,bg="#C0392B",fg="white",command=lambda:ShowDialogs(3))
button3.grid(row=0,column=2,sticky="nsew",padx=10,pady=10)

button3=Button(frame,text="Dining philosopher analyse",padx=10,pady=10,bg="#C0392B",fg="white",command=lambda:ShowDialogs(4))
button3.grid(row=0,column=3,sticky="nsew",padx=10,pady=10)

frame.grid_columnconfigure(0,weight=1)
frame.grid_columnconfigure(1,weight=1)
frame.grid_columnconfigure(2,weight=1)
frame.grid_columnconfigure(3,weight=1)
frame.grid_columnconfigure(4,weight=1)


window.mainloop()