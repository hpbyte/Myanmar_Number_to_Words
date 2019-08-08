# Myanmar Number to Words

Basically, this is a simple python script for converting Myanmar numbers into Myanmar spoken words
It is expected to be able to detect and convert the following types:
  - Dates (DD-MM-YYYY or DD/MM/YYYY)
  - Time (H:mm)
  - Digit Number
  - Decimal Number
  - Range
  - Fraction
  - NRC
  - Amount

This is an essential part in the preprocessing stage of the Myanmar Text-to-Speech Project in which the numbers in the text dataset needs to be converted into spoken words.

## Examples

```
# Amount
၁၀၇         =>  တစ်ရာ့ ခုနှစ်
၁၂၀         =>  တစ်ရာ့ နှစ်ဆယ်
၃၂၁         =>  သုံ:ရာ နှစ်ဆယ့် တစ်
၃၂၅၉၇၀၀၀၃၀  =>  သုံ:သောင်: နှစ်ထောင့် ငါ:ရာ ကို:ဆယ့် ခုနှစ်သိန်: သုံ:ဆယ်
၅၀,၀၅၁,၂၃၀  =>  သိန်: ငါ:ရာ ငါ:သောင်: တစ်ထောင့် နှစ်ရာ့ သုံ:ဆယ်


# Phone Number
၀၁၅၂၈၈၂၃    =>  သုည တစ် ငါ: နှစ် ရှစ် ရှစ် နှစ် သုံ:


# Date (DD-MM-YYYY or DD/MM/YYYY)
၁၅-၁၂-၂၀၁၉  =>  နှစ်ထောင့် ဆယ့် ကို: ခုနှစ် ဆယ့် နှစ် လပိုင်: ဆယ့် ငါ: ရက်


# Time (H:mm)
၃:၂၅        =>  သုံ: နာရီ နှစ်ဆယ့် ငါ: မိနစ်
၄:၃၀        =>  လေ: နာရီ ခွဲ


# Decimal
၃၂.၄၂၈      =>  သုံ:ဆယ့် နှစ် ဒဿမ လေ: နှစ် ရှစ်
```

## Usage

Clone or download this repository
```
git clone https://github.com/hpbyte/Myanmar_Number_to_Words.git
```

You will see two files under the cloned directory
```
Myanmar_Number_to_Words
  | mm_num2word.py
  | convert.py
```

`mm_num2word.py` contains all the logics needed (from extracting numbers from a string to detecting and converting).

`convert.py` is the tool that is able to take an input file, transform the numbers from the file into words accordingly and then output the result file.

```
python3 convert.py --input path/to/your/input.txt --output path/for/output.txt 
```
