
import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

    response = requests.get(URL)
    return response.content
  
  def program_agencies(self):
    # we use the JSON library to parse the API response into nicely formatted JSON
        programs_list = []
        try:
            programs = json.loads(self.get_programs())
            if isinstance(programs, list):
                for program in programs:
                    if isinstance(program, dict) and "agency" in program:
                        programs_list.append(program["agency"])
                    else:
                        print(f"Ignoring invalid program entry: {program}")
            else:
                print(f"Unexpected API response format: {programs}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

        
        return programs_list

programs = GetPrograms()
agencies = programs.program_agencies()

for agency in set(agencies):
    print(agency)


# programs = GetPrograms().get_programs()
# print(programs)

