def main():

    spacecraft = {"name" : "James Webb Space Telescope", "distance" : "0.01"}
    #spacecraft.update({"orbit" : "sun"})
    print(create_report(spacecraft))

def create_report(spacecraft):

    return f""" 
============ REPORT ============

Name: {spacecraft["name"]}

Distance: {spacecraft["distance"]} AU

Orbit: {spacecraft.get("orbit", "Unknown")}

================================
"""


main()
