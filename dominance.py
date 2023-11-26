#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 17:07:39 2023

@author: sofiat
"""

from enumerateSMs import EnumerateStableMatchings

class SPASDominance:
    def __init__(self, filename):
        self.filename = filename
        E = EnumerateStableMatchings((self.filename))
        E.choose(1)
        matchings = E.stable_matchings
        self.stable_matchings = dict()
        for idx, SM in enumerate(matchings, 1):
            self.stable_matchings[f"M{idx}"] = SM
        #self.stable_matchings = [{'s1': 'p1', 's2': 'p2', 's3': 'p3', 's4': 'p3', 's5': 'p4', 's6': 'p5', 's7': 'p1', 's8': 'p1', 's9': 'p6', 's10': 'p6', 's11': 'p7', 's12': 'p7', 's13': 'p8', 's14': 'p8'}, {'s1': 'p1', 's2': 'p2', 's3': 'p3', 's4': 'p3', 's5': 'p4', 's6': 'p5', 's7': 'p1', 's8': 'p1', 's9': 'p6', 's10': 'p6', 's11': 'p8', 's12': 'p7', 's13': 'p8', 's14': 'p7'}, {'s1': 'p1', 's2': 'p2', 's3': 'p3', 's4': 'p3', 's5': 'p4', 's6': 'p5', 's7': 'p1', 's8': 'p1', 's9': 'p6', 's10': 'p6', 's11': 'p8', 's12': 'p8', 's13': 'p7', 's14': 'p7'}, {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p3', 's5': 'p4', 's6': 'p5', 's7': 'p1', 's8': 'p1', 's9': 'p6', 's10': 'p6', 's11': 'p7', 's12': 'p7', 's13': 'p8', 's14': 'p8'}, {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p3', 's5': 'p4', 's6': 'p5', 's7': 'p1', 's8': 'p1', 's9': 'p6', 's10': 'p6', 's11': 'p8', 's12': 'p7', 's13': 'p8', 's14': 'p7'}, {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p3', 's5': 'p4', 's6': 'p5', 's7': 'p1', 's8': 'p1', 's9': 'p6', 's10': 'p6', 's11': 'p8', 's12': 'p8', 's13': 'p7', 's14': 'p7'}, {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p3', 's5': 'p4', 's6': 'p5', 's7': 'p6', 's8': 'p1', 's9': 'p6', 's10': 'p1', 's11': 'p7', 's12': 'p7', 's13': 'p8', 's14': 'p8'}, {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p3', 's5': 'p4', 's6': 'p5', 's7': 'p6', 's8': 'p1', 's9': 'p6', 's10': 'p1', 's11': 'p8', 's12': 'p7', 's13': 'p8', 's14': 'p7'}, {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p3', 's5': 'p4', 's6': 'p5', 's7': 'p6', 's8': 'p1', 's9': 'p6', 's10': 'p1', 's11': 'p8', 's12': 'p8', 's13': 'p7', 's14': 'p7'}, {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p3', 's5': 'p4', 's6': 'p5', 's7': 'p6', 's8': 'p6', 's9': 'p1', 's10': 'p1', 's11': 'p7', 's12': 'p7', 's13': 'p8', 's14': 'p8'}, {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p3', 's5': 'p4', 's6': 'p5', 's7': 'p6', 's8': 'p6', 's9': 'p1', 's10': 'p1', 's11': 'p8', 's12': 'p7', 's13': 'p8', 's14': 'p7'}, {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p3', 's5': 'p4', 's6': 'p5', 's7': 'p6', 's8': 'p6', 's9': 'p1', 's10': 'p1', 's11': 'p8', 's12': 'p8', 's13': 'p7', 's14': 'p7'}, {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p4', 's5': 'p5', 's6': 'p3', 's7': 'p1', 's8': 'p1', 's9': 'p6', 's10': 'p6', 's11': 'p7', 's12': 'p7', 's13': 'p8', 's14': 'p8'}, {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p4', 's5': 'p5', 's6': 'p3', 's7': 'p1', 's8': 'p1', 's9': 'p6', 's10': 'p6', 's11': 'p8', 's12': 'p7', 's13': 'p8', 's14': 'p7'}, {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p4', 's5': 'p5', 's6': 'p3', 's7': 'p1', 's8': 'p1', 's9': 'p6', 's10': 'p6', 's11': 'p8', 's12': 'p8', 's13': 'p7', 's14': 'p7'}, {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p4', 's5': 'p5', 's6': 'p3', 's7': 'p6', 's8': 'p1', 's9': 'p6', 's10': 'p1', 's11': 'p7', 's12': 'p7', 's13': 'p8', 's14': 'p8'}, {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p4', 's5': 'p5', 's6': 'p3', 's7': 'p6', 's8': 'p1', 's9': 'p6', 's10': 'p1', 's11': 'p8', 's12': 'p7', 's13': 'p8', 's14': 'p7'}, {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p4', 's5': 'p5', 's6': 'p3', 's7': 'p6', 's8': 'p1', 's9': 'p6', 's10': 'p1', 's11': 'p8', 's12': 'p8', 's13': 'p7', 's14': 'p7'}, {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p4', 's5': 'p5', 's6': 'p3', 's7': 'p6', 's8': 'p6', 's9': 'p1', 's10': 'p1', 's11': 'p7', 's12': 'p7', 's13': 'p8', 's14': 'p8'}, {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p4', 's5': 'p5', 's6': 'p3', 's7': 'p6', 's8': 'p6', 's9': 'p1', 's10': 'p1', 's11': 'p8', 's12': 'p7', 's13': 'p8', 's14': 'p7'}, {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p4', 's5': 'p5', 's6': 'p3', 's7': 'p6', 's8': 'p6', 's9': 'p1', 's10': 'p1', 's11': 'p8', 's12': 'p8', 's13': 'p7', 's14': 'p7'}]
        # copy over stable matchings to save time from generating them every time we hit run
        #self.stable_matchings = {'M1': {'s1': 'p1', 's2': 'p2', 's3': 'p3', 's4': 'p3', 's5': 'p4', 's6': 'p5', 's7': 'p1', 's8': 'p1', 's9': 'p6', 's10': 'p6', 's11': 'p7', 's12': 'p7', 's13': 'p8', 's14': 'p8'}, 'M2': {'s1': 'p1', 's2': 'p2', 's3': 'p3', 's4': 'p3', 's5': 'p4', 's6': 'p5', 's7': 'p1', 's8': 'p1', 's9': 'p6', 's10': 'p6', 's11': 'p8', 's12': 'p7', 's13': 'p8', 's14': 'p7'}, 'M3': {'s1': 'p1', 's2': 'p2', 's3': 'p3', 's4': 'p3', 's5': 'p4', 's6': 'p5', 's7': 'p1', 's8': 'p1', 's9': 'p6', 's10': 'p6', 's11': 'p8', 's12': 'p8', 's13': 'p7', 's14': 'p7'}, 'M4': {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p3', 's5': 'p4', 's6': 'p5', 's7': 'p1', 's8': 'p1', 's9': 'p6', 's10': 'p6', 's11': 'p7', 's12': 'p7', 's13': 'p8', 's14': 'p8'}, 'M5': {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p3', 's5': 'p4', 's6': 'p5', 's7': 'p1', 's8': 'p1', 's9': 'p6', 's10': 'p6', 's11': 'p8', 's12': 'p7', 's13': 'p8', 's14': 'p7'}, 'M6': {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p3', 's5': 'p4', 's6': 'p5', 's7': 'p1', 's8': 'p1', 's9': 'p6', 's10': 'p6', 's11': 'p8', 's12': 'p8', 's13': 'p7', 's14': 'p7'}, 'M7': {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p3', 's5': 'p4', 's6': 'p5', 's7': 'p6', 's8': 'p1', 's9': 'p6', 's10': 'p1', 's11': 'p7', 's12': 'p7', 's13': 'p8', 's14': 'p8'}, 'M8': {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p3', 's5': 'p4', 's6': 'p5', 's7': 'p6', 's8': 'p1', 's9': 'p6', 's10': 'p1', 's11': 'p8', 's12': 'p7', 's13': 'p8', 's14': 'p7'}, 'M9': {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p3', 's5': 'p4', 's6': 'p5', 's7': 'p6', 's8': 'p1', 's9': 'p6', 's10': 'p1', 's11': 'p8', 's12': 'p8', 's13': 'p7', 's14': 'p7'}, 'M10': {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p3', 's5': 'p4', 's6': 'p5', 's7': 'p6', 's8': 'p6', 's9': 'p1', 's10': 'p1', 's11': 'p7', 's12': 'p7', 's13': 'p8', 's14': 'p8'}, 'M11': {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p3', 's5': 'p4', 's6': 'p5', 's7': 'p6', 's8': 'p6', 's9': 'p1', 's10': 'p1', 's11': 'p8', 's12': 'p7', 's13': 'p8', 's14': 'p7'}, 'M12': {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p3', 's5': 'p4', 's6': 'p5', 's7': 'p6', 's8': 'p6', 's9': 'p1', 's10': 'p1', 's11': 'p8', 's12': 'p8', 's13': 'p7', 's14': 'p7'}, 'M13': {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p4', 's5': 'p5', 's6': 'p3', 's7': 'p1', 's8': 'p1', 's9': 'p6', 's10': 'p6', 's11': 'p7', 's12': 'p7', 's13': 'p8', 's14': 'p8'}, 'M14': {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p4', 's5': 'p5', 's6': 'p3', 's7': 'p1', 's8': 'p1', 's9': 'p6', 's10': 'p6', 's11': 'p8', 's12': 'p7', 's13': 'p8', 's14': 'p7'}, 'M15': {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p4', 's5': 'p5', 's6': 'p3', 's7': 'p1', 's8': 'p1', 's9': 'p6', 's10': 'p6', 's11': 'p8', 's12': 'p8', 's13': 'p7', 's14': 'p7'}, 'M16': {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p4', 's5': 'p5', 's6': 'p3', 's7': 'p6', 's8': 'p1', 's9': 'p6', 's10': 'p1', 's11': 'p7', 's12': 'p7', 's13': 'p8', 's14': 'p8'}, 'M17': {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p4', 's5': 'p5', 's6': 'p3', 's7': 'p6', 's8': 'p1', 's9': 'p6', 's10': 'p1', 's11': 'p8', 's12': 'p7', 's13': 'p8', 's14': 'p7'}, 'M18': {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p4', 's5': 'p5', 's6': 'p3', 's7': 'p6', 's8': 'p1', 's9': 'p6', 's10': 'p1', 's11': 'p8', 's12': 'p8', 's13': 'p7', 's14': 'p7'}, 'M19': {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p4', 's5': 'p5', 's6': 'p3', 's7': 'p6', 's8': 'p6', 's9': 'p1', 's10': 'p1', 's11': 'p7', 's12': 'p7', 's13': 'p8', 's14': 'p8'}, 'M20': {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p4', 's5': 'p5', 's6': 'p3', 's7': 'p6', 's8': 'p6', 's9': 'p1', 's10': 'p1', 's11': 'p8', 's12': 'p7', 's13': 'p8', 's14': 'p7'}, 'M21': {'s1': 'p2', 's2': 'p3', 's3': 'p1', 's4': 'p4', 's5': 'p5', 's6': 'p3', 's7': 'p6', 's8': 'p6', 's9': 'p1', 's10': 'p1', 's11': 'p8', 's12': 'p8', 's13': 'p7', 's14': 'p7'}}
        
        # copy over useful data structures from enumerateSMs
        self.student_dict = E.sp
        self.project_dict = E.plc
        self.lecturer_dict = E.lp
        self.lp_rank = E.lp_rank
        self.proj_rank = E.proj_rank
        
    
    def dominates(self, M, Mprime):
        # extract the stable matching corresponding to the input
        M_matching = self.stable_matchings[M]
        Mprime_matching = self.stable_matchings[Mprime]
        # to keep track of how many students prefer one matching over the other
        M_dominates_Mprime = 0
        Mprime_dominates_M = 0
        for student in M_matching:
            M_project = M_matching[student]
            Mprime_project = Mprime_matching[student]
            # if student is unassigned or has the same project in both matching
            if M_project == '' or (M_project == Mprime_project):
                continue
            else:
                M_project_rank = self.student_dict[student][1][M_project]
                Mprime_project_rank = self.student_dict[student][1][Mprime_project]                
                if M_project_rank < Mprime_project_rank: # i.e., student prefers M to Mprime
                    M_dominates_Mprime += 1
                else:
                    Mprime_dominates_M += 1
                
        # as long as we are not checking exactly the same matching against itself
        # both M_dominates_Mprime and Mprime_dominates_M should not be 0 at this point
        if M_dominates_Mprime > 0 and Mprime_dominates_M == 0:
            return True
            #return f"{M} dominates {Mprime}: True --> {M_dominates_Mprime} {Mprime_dominates_M}"
        else:
            return False
            #return f"{M} dominates {Mprime}: False --> {M_dominates_Mprime} {Mprime_dominates_M}"
        
    def dominance(self):
        # this assumes that the first stable matching from the 
        # enumerate list is student-optimal
        dominance_graph = dict()
        matchings = list(self.stable_matchings.keys())
        for idx1 in range(len(matchings)):
            dominance_graph[matchings[idx1]] = set()
            for idx2 in range(idx1+1, len(matchings)):                
                if self.dominates(matchings[idx1], matchings[idx2]) is True:
                    dominance_graph[matchings[idx1]].add(matchings[idx2])
            # if the current matching M' is dominated by an existing matching M
            # then remove all the vertices that M' points to from M
            current_vertex = matchings[idx1]
            for vertex in dominance_graph:
                neighbours = dominance_graph[vertex]
                if current_vertex in neighbours:
                    current_vertex_neighbours = dominance_graph[current_vertex]
                    new_neighbours = neighbours.difference(current_vertex_neighbours)
                    dominance_graph[vertex] = new_neighbours
        return dominance_graph
        
    
filename = "spas_lattice.txt"
d = SPASDominance(filename)
SMs = d.stable_matchings
#  print the stable matchings
for k, v in SMs.items():
    print(f"=== {k} ===")
    for i, j in v.items():
        print(f"{i} ---> {j}")
    print()

# print the dominance graph
dg = d.dominance()
for k, v in dg.items():
    print(f"{k} dominates {v}")    