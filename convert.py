import os
import argparse
from mm_num2word import mm_num2word, extract_num

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--input', required=True)
  parser.add_argument('--output', default='out.txt')
  args = parser.parse_args()

  in_file = os.path.abspath(args.input)
  out_file = os.path.abspath(args.output)

  with open(in_file, encoding='utf-8') as f_in:
    with open(out_file, mode='w', encoding='utf-8') as f_out:
      for line in f_in:
        nums = extract_num(line)
        for n in nums:
          line = line.replace(n, mm_num2word(n))
          
        f_out.write(line)

if __name__ == '__main__':
  main()
