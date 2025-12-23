# import qrcode
# img = qrcode.make("www.google.com")
# img.save("Google.jpg")

# with open("web.csv", "r") as f :
#     for i in f :
#         print(i)


import qrcode
with open("web.csv", "r") as f :
    for i in f :
        data = i.strip("\n")
        new_data = data.split(",")
        print(new_data) # aita amnitei disi
        img = qrcode.make(f"{new_data[1]}")
        img.save(f"{new_data[0]}.jpg")






# l = ["site", "www.google.com"]
# print(l[0])
# print(l[1])
