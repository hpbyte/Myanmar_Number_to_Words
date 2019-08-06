import re

def convert_digit(num):
  """
  For Digit Numbers

  @type     num   str
  @param    num   Myanmar digit number
  @rtype          str
  @return         converted Myanmar spoken words
  """

  mm_digit = {
    '၁': 'တစ်',
    '၂': 'နှစ်',
    '၃': 'သုံ:',
    '၄': 'လေ:',
    '၅': 'ငါ:',
    '၆': 'ခြောက်',
    '၇': 'ခုနှစ်',
    '၈': 'ရှစ်',
    '၉': 'ကို:'
  }

  converted = ''
  nb_digits = len(num)

  def check_if_zero(pos):
    return not num[-pos] == '၀'

  def hundred_thousandth_val():
    n = num[:-5]
    return ('သိန်: ' + mm_num2word(n)) if (n[-2:] == '၀၀') else (mm_num2word(n) + 'သိန်: ')

  def thousandth_val():
    return mm_digit[num[-4]] + ('ထောင် ' if (num[-3:] == '၀၀၀') else 'ထောင့် ')

  def hundredth_val():
    return mm_digit[num[-3]] + ('ရာ့ ' if (
      (num[-2] == '၀' and re.match(r'[၁-၉]', num[-1])) or (re.match(r'[၁-၉]', num[-2]) and num[-1] == '၀')
    ) else 'ရာ ')

  def tenth_val():
    return ('' if (num[-2] == '၁') else mm_digit[num[-2]]) + ('ဆယ် ' if (num[-1] == '၀') else 'ဆယ့် ')

  if ((nb_digits > 5)):
    converted += hundred_thousandth_val()
  if ((nb_digits > 4) and check_if_zero(5)):
    converted += mm_digit[num[-5]] + 'သောင်: '
  if ((nb_digits > 3) and check_if_zero(4)):
    converted += thousandth_val()
  if ((nb_digits > 2) and check_if_zero(3)):
    converted += hundredth_val()
  if ((nb_digits > 1) and check_if_zero(2)):
    converted += tenth_val()
  if ((nb_digits > 0) and check_if_zero(1)):
    converted += mm_digit[num[-1]]

  return converted

def mm_num2word(num):
  """
  @type     num   str
  @param    num   Myanmar number
  @rtype          str
  @return         converted Myanmar spoken words
  """

  # digits
  word = convert_digit(num)

  return word
