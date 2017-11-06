from venues.exceptions import InvalidUserSelectionError


class VenuesSelector(object):
    def __init__(self, feed_data):
        self.feed_data = feed_data
        self.users = self.feed_data['users']
        self.venues = self.feed_data['venues']
        self.users_by_name = self._index_by_name(self.users)
        self.venues_by_name = self._index_by_name(self.venues)

    def select_venues(self, user_names):
        self._validate_user_selection(user_names)
        venues_to_avoid = {}
        for venue in self.venues:
            venues_to_avoid.update({venue['name']: {'nothing_to_eat': [], 'nothing_to_drink': []}})
            for name in user_names:
                if not self._something_to_drink(name, venue):
                    venues_to_avoid[venue['name']]["nothing_to_drink"].append(name)
                if not self._something_to_eat(name, venue):
                    venues_to_avoid[venue['name']]["nothing_to_eat"].append(name)

        venues_to_avoid = {k: v for k, v in venues_to_avoid.items() if v['nothing_to_eat'] or v['nothing_to_drink']}
        safe_venues = list(set(self.venues_by_name.keys()).difference(set(venues_to_avoid.keys())))

        return {"safe": safe_venues, "to_avoid": venues_to_avoid}

    def get_user_names(self):
        return self.users_by_name.keys()

    def _validate_user_selection(self, user_names):
        if not user_names:
            raise InvalidUserSelectionError("Please select some users")
        elif set(user_names).intersection(set(self.users_by_name.keys())) != set(user_names):
            raise InvalidUserSelectionError("Please select valid users")

    def _something_to_drink(self, name, venue):
        return set(map(str.lower, self.users_by_name[name]['drinks'])).intersection(set(map(str.lower,venue['drinks'])))

    def _something_to_eat(self, name, venue):
        return set(map(str.lower, venue['food'])).difference(set(map(str.lower, self.users_by_name[name]['wont_eat'])))

    @staticmethod
    def _index_by_name(data):
        data_by_name = {}
        for item in data:
            data_by_name[item['name']] = {k: v for k, v in item.items() if k is not "name"}
        return data_by_name
