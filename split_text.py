import sys

def outputs():
  n = 1
  while True:
    print(n)
    yield open('div{0:03d}.txt'.format(n), 'wb') 
    n += 1

def split_file(path, lim=5000000):
  out = outputs()
  with open(path, 'r') as f:
    lines = f.readlines()
    div = len(lines)//lim
    rem = 1 if(len(lines)%lim) > 0 else 0
    num = div + rem
    print("len = ", len(lines))
    print("num = ", div, " + ", rem)
    for i in range(num):
      file = next(out)
      it = i*lim
      file.write("".join(lines[it:it+lim if it+lim <= len(lines) else it+(len(lines)%lim)]).encode('utf-8'))
      file.close()

if __name__ == '__main__':
  split_file('data_test.txt', 50)