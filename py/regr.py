import sys
import os
import re
import glob

def gen_get_files(basedir=".", mask="*.*"):
    """Generator function returning list of image files in directory according to file mask specification """
    for root, dir, files in os.walk(basedir):
        for f in glob.iglob(os.path.join(root, mask)):
            assert os.path.isfile(f), "File '%s' does not exist!" % f
            yield f 

def gen_test_cases(regr_files):
    for rfile in regr_files:
        dirname = os.path.dirname(rfile)
        fr = open(rfile, 'r')
        for line in (x.strip() for x in fr.readlines()):
            if line == '' or line.startswith('#'): continue
            test_file = os.path.join(dirname, line.strip())
            yield test_file
        fr.close()

def gen_filter_tc_names(output, filename):
    dirname = os.path.dirname(filename)
    p = re.compile("^([^']*')([a-zA-Z0-9_.-]*')[ \t]*(.*)$")
    for line in output:
        matched = p.match(line)
        if matched:
            prefix, filename, suffix = matched.groups()
            new_filename = os.path.join(dirname, filename)
            yield prefix + new_filename.ljust(60) + suffix
        else:
            if 'No handlers could be found for logger' in line: continue
            yield line

def gen_get_tc_results(input_):
    p = re.compile("^.*([0-9]*)[ \t]*([0-9]*)[ \t]*(Passed|Failed)[ \t]*$")
    for line in input_:
        matched = p.match(line)
        if matched:
            # TODO: parse matched string and get numbers
            yield (0, 0, line)
        else:
            yield (0, 0, line)

                
def main():
    try:
        input_name = sys.argv[1]
    except IndexError:
        input_name = '.'

    if os.path.isdir(input_name):
        gtcs = gen_test_cases(gen_get_files(input_name, '.regr'))
        counter = 0
        for counter, tc in enumerate(gtcs, 1):
            cmdline = 'python %s' % os.path.abspath(tc)
            os.system(cmdline)
        print "Total %i test cases were executed ..." % counter
    else:
        pass
        

if __name__ == "__main__":
    main()
