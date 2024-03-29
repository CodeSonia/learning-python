file = open("output.txt", "w")

text_1 = "Sherlock Holmes took his bottle from the corner of the mantel-piece and his hypodermic syringe from its neat morocco case. With his long, white, nervous fingers he adjusted the delicate needle, and rolled back his left shirt-cuff. For some little time his eyes rested thoughtfully upon the sinewy forearm and wrist all dotted and scarred with innumerable puncture-marks. Finally he thrust the sharp point home, pressed down the tiny piston, and sank back into the velvet-lined arm-chair with a long sigh of satisfaction."

text_2 = "Three times a day for many months I had witnessed this performance, but custom had not reconciled my mind to it."

file.write(text_1)
file.write("\n")
file.write(text_2)
file.write("\n")

file.writelines([text_1, "\n", text_2])

file.close()
