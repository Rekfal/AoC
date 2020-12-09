import re

def validator(passport):
    requiredfields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    passportdata = {}
    allfields = []
    for entry in passport:
        fieldvalue = entry.split(":")
        field = fieldvalue[0]
        value = fieldvalue[1]

        passportdata[field] = value
        allfields.append(field)

    for rule in requiredfields:
        if rule not in allfields:
            return False
    
    for field in passportdata:
        if field == "byr":
            if int(passportdata[field]) < 1920 or int(passportdata[field]) > 2002:
                return False

        if field == "iyr":
            if int(passportdata[field]) < 2010 or int(passportdata[field]) > 2020:
                return False

        if field == "eyr":
            if int(passportdata[field]) < 2020 or int(passportdata[field]) > 2030:
                return False

        if field == "hgt":
            result = re.search(r"(\d+)(in|cm)", str(passportdata[field]))
            if result == None:
                return False
            if result.group(2) == "in":
                if int(result.group(1)) < 59 or  int(result.group(1)) > 76:
                    return False
            if result.group(2) == "cm":
                if int(result.group(1)) < 150 or  int(result.group(1)) > 193:
                    return False

        if field == "hcl":
            result = re.match(r"#\w\w\w\w\w\w", passportdata[field])
            if result == None:
                return False

        if field == "ecl":
            eyecolors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if passportdata[field] not in eyecolors:
                return False
        
        if field == "pid":
            if len(passportdata[field]) != 9:
                return False
                
    return True

with open("day4.txt") as f:
    data = f.read().split("\n")
    allpassports = []
    passport = ""
    for entry in data:
        if passport != "":
            passport += " "
        passport += entry
        if entry == "":
            passport = passport[:-1]
            passportdata = passport.split(" ")
            allpassports.append(passportdata)
            passport = ""

    validcount = 0
    for passport in allpassports:
        if (validator(passport)):
            validcount += 1
    print(validcount)
