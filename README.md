# PBFT CONSENSUS

Performed a simulation of the PBFT Consensus Algorithm, over a Road Network containing RSU(Road Side Units) and Crowdsourced
OBU(OnBoard Unit) and the algorithm is n/3 fault tolerant.

A query is made in the form of [source,destination].

The various steps are as follows:
PhaseI: Given N nodes ,choose a leader and rest of others are backups and then preprepare message(encrypted) is sent.

PhaseII: Check for valid message.

PhaseIII: if a node has correct message more than (2*f + 1) then that node sends the final commit message to rest.

Final commit: Returns the most occured correct message as output.

The algorithm reaches a consensus and gives back the result.

## Getting Started

Clone the repository.

Run the main.py file to see the algorithm in action.


## Built With

* NetworkX - The network Visualization library of Python.


