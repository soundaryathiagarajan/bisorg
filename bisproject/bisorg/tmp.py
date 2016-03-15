import requests 
import tika_new
from tika import parser

def download_file(url):
    """
    Download any doc file 
    """
    print "Download the file %s"%url
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return local_filename

def process_pdf(local_filename):
    #Put it try block, and return the content
	parsed = tika_new.parsePDF(local_filename)
	# parsed["metadata"]
	return parsed["content"].strip()

if __name__ == "__main__":
    results = []
    t1 = {'author':'Soundarya',"link":"https://www.bis.org/review/r150806a.htm","posted_date":"2014-03-01"}
    t2 = {'author':'Sairam',"link":"https://www.bis.org/review/r150730b.pdf","posted_date":"2014-01-01"}
    results.append(t1)
    results.append(t2)
    for x in results:
        print 'link is:'+x['link']
        print 'Author Name:' +x['author']
        #for downloading the file 
        ha = download_file(x['link'])
        pa = process_pdf(ha)
        
        print pa
    # b = download_file("https://www.bis.org/review/r150807a.pdf")
    # print b
    # process_pdf(b)