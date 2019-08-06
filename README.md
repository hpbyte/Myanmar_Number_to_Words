# mm_num2word

- Basically, this is a simple python script for converting Myanmar numbers into Myanmar spoken words
- It is expected to be able to detect and convert the following types (Currently only digits):
  - Dates
  - Time
  - Digit Number
  - Cardinal Number
  - Range
  - Fraction
  - NRC
  - Money

```
# Digits
၁၀၇         =>  တစ်ရာ့ ခုနှစ်
၁၂၀         =>  တစ်ရာ့ နှစ်ဆယ်
၃၂၁         =>  သုံ:ရာ နှစ်ဆယ့် တစ်
၃၂၅၉၇၀၀၀၃၀  =>  သုံ:သောင်: နှစ်ထောင့် ငါ:ရာ ကို:ဆယ့် ခုနှစ်သိန်: သုံ:ဆယ်
၅၀၀၅၁၂၃၀    =>  သိန်: ငါ:ရာ ငါ:သောင်: တစ်ထောင့် နှစ်ရာ့ သုံ:ဆယ်
```