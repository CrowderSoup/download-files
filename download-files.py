import os, os.path, urllib.request, sys, getopt

def main(argv):
    print(argv)
    input_file = ''
    download_dir = ''
    try:
        opts, args = getopt.getopt(argv,
                                    "hi:d:",
                                    ["input-file=","download-dir="])
    except getopt.GetoptError as err:
        print(err)
        print('download-files.py -i <input-file> -d <download-directory>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('download-files.py -i <input-file> -d <download-directory>')
            sys.exit()
        elif opt in ("-i", "--input-file"):
            input_file = arg
        elif opt in ("-d", "--download-dir"):
            download_dir = arg

    if(input_file != ''):
        print("Opening input file...")
        links = open(input_file, 'r')
    else:
        print("No Input file specified, trying default...")
        links = open("urls.txt", 'r')

    for link in links:
        link = link.strip()
        name = link.rsplit('/', 1)[-1]

        if(download_dir == ''):
            print("Download Directory not provided... using default.")
            download_dir = os.getcwd() + '\downloads'

        filename = os.path.join(download_dir, name)

        if not os.path.isfile(filename):
            print('Downloading: ' + filename)
            try:
                urllib.request.urlretrieve(link, filename)
            except Exception as inst:
                print(inst)
                print('Continuing...')

if __name__ == "__main__":
   main(sys.argv[1:])
