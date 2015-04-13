#!/usr/bin/python
import sys,os
def make_html(folder_path):
    folder_location = folder_path
    html_folder = folder_location + "/html"
    if not os.path.exists(html_folder):
        os.mkdir(html_folder)

    os.system("rm -rf " + html_folder + "/*.html")
    os.system("rm -rf " + html_folder + "/.g*")

    for file_name in os.listdir(folder_location):
        html_file_name = html_folder + "/" + file_name + ".html"
        file_name = folder_location + "/" + file_name
        if os.path.isdir(file_name) or "~" in file_name:
            continue
        f = open(file_name,"r")
        html = open(html_file_name,"w")
        html.write("<html><body style='margin:100;padding:10'>")
	html.write("<center><h1><font color='red'>"+ file_name.split("/").pop().split(".")[0]+"</font></h1></center>")
        count = 0
        for line in f:
	    if  line.startswith("\t\t") or line.startswith('        ') :
                html.write("<h3><font color='olive'>")
                html.write(str(count) + "." + str(count_inner) + " : " + line.strip())
                html.write("</font></h3>")
                count_inner = count_inner + 1

            elif  line.startswith("\t") or line.startswith('    ') :
	        count_inner = 1
                count = count + 1
                html.write("<h2><font color='teal'>")
                html.write(str(count) + " : " + line.strip())
                html.write("</font></h2>")
	    elif line.strip().startswith("http://"):
		html.write("<a href=" + line.strip() + ">" + line + "</a>")
                html.write("</br>")
            else:
                html.write("\t" + line.strip())
                html.write("</br>")
            
        html.write("</body></html>")
        f.close()
        html.close()

if (__name__ == "__main__"):
	folder = sys.argv[1]
	print "Converting all docs in "+folder + " to html"
	make_html(folder)
