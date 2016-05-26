# from collections import OrderedDict
# from django.utils.datastructures import OrderedSet
class DequeSet:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def append(self, item):
        self.items.append(item)

    def pop_from_front(self):
        return self.items.pop(0)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class FSM:
    def __init__(self):
        self._startstate = None
        self._acceptstates = set()
        self._states_and_trans = dict()

    # statename is a string, the name of state
    def setstartstate(self, statename):
        if statename in self._states_and_trans:
            self._startstate = statename

    # Adds the state named StateName to the set of accept states.
    # That state must already by one of the states
    def setacceptstate(self, statename):
        if statename in self._states_and_trans:
            self._acceptstates.add(statename)

    # Adds the state named StateName to the FSM.
    def addstate(self, statename):
        self._states_and_trans[statename] = set()

    # fromstate and tostate are the strings labeling the states in the transition.
    # label should be a single character.
    def addtransition(self, fromstate, tostate, label):
        if (fromstate in self._states_and_trans) and (tostate in self._states_and_trans) and len(label)==1:
            self._states_and_trans[fromstate].add((tostate, label))

    def accepts(self, string):
        if len(self._acceptstates)==0:
            return False
        string_to_check = list(string)
        checking = 0
        checked = set()
        end = len(string_to_check)
        queue = DequeSet()
        queue.enqueue(((self._startstate, None), 0))
        while not all_end_vertices_same(queue, end):
            popped = queue.pop_from_front()
            current = popped[0][0]
            checking = popped[1]
            for i in self._states_and_trans[current]:
                if i[1]==string_to_check[checking]:
                    if not (i, checking+1) in checked:
                        checked.add((i, checking+1))
                        queue.enqueue((i, checking+1))
        if queue.size()==0:
            return False
        for tup in queue.items:
            if tup[0][0] in self._acceptstates:
                return True
            else:
                pass
        return False


def all_end_vertices_same(queue_of_tuples, val):
    if queue_of_tuples.size()==0:
        return True
    else:
        for i in queue_of_tuples.items:
            if i[1]==val:
                return True
            else:
                return False
