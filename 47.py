#convert digit/numbers to word
def number_to_words(n):
    ones = ["zero", "one", "two", "three", "four", "five",
            "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen",
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]
    if n < 10:
        return ones[n]
    elif n < 20:
        return teens[n - 10]
    elif n<100:
        return tens[n//10]+(""if n%10==0 else "-" +ones[n%10])
    elif n<1000: 
        return ones[n//100]+" hundred "+(""if n%100==0 else " " +number_to_words(n%100))
    elif n<10000:
        return ones[n//1000]+" thousand "+(""if n%1000==0 else " " +number_to_words(n%1000))
    else:
        return ("number too large(max(9999))")
num = int(input("Enter a number (0-9999): "))
print("In words:", number_to_words(num))