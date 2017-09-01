import numpy as np
import scipy.io

def cstream2cevent(cstream):
    cevent = np.array([[-1, -1, -1]], dtype=np.float64)
    numrows, numcols = np.shape(cstream)
    if numcols > 2:
        return cstream
    in_event = False
    prev_category = 0
    build_event = np.array([[-1, -1, -1]], dtype=np.float64)
    for c in range(0, numrows):
        cur_category = cstream[c, 1]
        if cur_category != prev_category:
            if build_event[0, 0] > 0:
                build_event[0, 1] = cstream[c, 0]
                build_event[0, 2] = prev_category
                cevent = np.append(cevent, build_event, axis=0)
                build_event = np.array([[-1, -1, -1]])
            elif cur_category > 0:
                build_event[0, 0] = cstream[c, 0]
        prev_category = cur_category
    return cevent[1:,:]

def event2cevent(data):
    numrows, numcols = np.shape(data)
    one_array = np.ones((numrows, 1), dtype=np.float64)
    return np.concatenate((data, one_array), axis=1)

def csv2np(filename):
    fid = open(filename, "r")
    lines = fid.readlines()
    fid.close()
    outarray = np.zeros(shape=(1,3), dtype=np.float64)
    for line in lines:
        line = line.split("\n")[0]
        npline = np.fromstring(line, dtype=np.float64, sep=',')
        outarray = np.concatenate((outarray, [npline]), axis=0)
    return outarray[1:,:]


def load_matfile(filename):
    return scipy.io.loadmat(filename)['sdata'][0][0][1]


fn = "C:/Users/sbf/Desktop/multiwork/experiment_70/included/__20140331_16579/derived/cevent_eye_roi_child.mat"
data = load_matfile(fn)
for i in range(0,1000):
    print(i)
    ind = data[:,0].argsort(axis=0)
    datay = data[ind,:]