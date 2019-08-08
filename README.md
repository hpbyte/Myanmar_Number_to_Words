# Myanmar Number to Words

- Basically, this is a simple python script for converting Myanmar numbers into Myanmar spoken words
- It is expected to be able to detect and convert the following types:
  - Dates
  - Time
  - Digit Number
  - Decimal Number
  - Range
  - Fraction
  - NRC
  - Amount

#### This is an essential part of the preprocessing stage of the Myanmar Text-to-Speech Project where the numbers in the text dataset needs to be converted into spoken words.

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