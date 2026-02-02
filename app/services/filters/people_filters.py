
class PeopleFilters:
    @staticmethod
    def define_filters(response: dict, params: dict):
        people = response["results"]

        if gender := params.get("gender"):
            people = PeopleFilters.filter_by_gender(people, gender)

        response["results"] = people
        return response

    
    @staticmethod
    def filter_by_gender(people: list, gender: str) -> list:
        gender = gender.lower()
        return [person for person in people if person.get("gender", "").lower() == gender]