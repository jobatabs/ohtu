class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True
        return False

class Not:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return True

class All:
    def __init__(self):
        pass

    def test(self, player):
        return True

class PlaysIn:
    def __init__(self, matcher, team):
        self._matcher = matcher
        self._team = team

    def test(self, player):
        return player.team == self._team and self._matcher.test(player)

class QueryBuilder:
    def __init__(self, matcher=All()):
        self.matcher = matcher
    
    def build(self):
        return self.matcher
    
    def plays_in(self, team):
        return QueryBuilder(PlaysIn(self.matcher, team))
    
    def has_at_least(self, value, attr):
        return QueryBuilder(HasAtLeast(self.matcher, value, attr))
    
    def has_fewer_than(self, value, attr):
        return QueryBuilder(HasFewerThan(self.matcher, value, attr))
    
    def one_of(self, matcher_1, matcher_2):
        return QueryBuilder(matcher_1)

class HasAtLeast:
    def __init__(self, matcher, value, attr):
        self._matcher = matcher
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value and self._matcher.test(player)

class HasFewerThan:
    def __init__(self, matcher, value, attr):
        self._matcher = matcher
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value and self._matcher.test(player)