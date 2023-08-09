text = "X-DSPAM-Confidence:    0.8475"

startPos = text.find(':') # slicing the text from this point in the sentance

piece = text[startPos+5:] # + counting the space between letters

end = float(piece)
print(piece)
print(end)
