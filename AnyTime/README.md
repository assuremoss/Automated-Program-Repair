---  
Title: Please hold on: more time = more patches? Automated program repair as anytime algorithms
Accepted at 2nd International Workshop on Automated Program Repair (APR 2021).

Authors:
  - name: Duc-Ly Vu 
    email: ducly.vu@unitn.it 
    affiliation: University of Trento (IT) 
  - name: Ivan Pashchenko 
    email: ivan.pashchenko@unitn.it 
    affiliation: University of Trento (IT) 
  - name: Fabio Massacci 
    email: fabio.massacci@ieee.org 
    affiliation: University of Trento (IT), Vrije Universiteit Amsterdam (NL) 
    
Abstract: "Current evaluations of automatic program repair
(APR) techniques focus on tools’ effectiveness, while little is
known about the practical aspects of using APR tools, such as
how long one should wait for a tool to generate a bug fix. In
this work, we empirically study whether APR tools are any time
algorithms (e.g., the more time they have, the more fixes they
generate, so it makes sense to trade off longer time for better
quality). Our preliminary experiment shows that the amount of
plausible patches, given exponentially greater time, only increases
linearly or not at all."

---  
[Camera-ready paper](https://github.com/lyvd/lyvd.github.io/blob/master/papers/apr2021.pdf), [Code](https://github.com/assuremoss/Automated-Program-Repair/tree/main/Anytime-Algorithm-2021), [Data](https://drive.google.com/drive/folders/1d0dYi6hIVaf5hi0gxexf0wbkLcJD_YZO?usp=sharing)

### Requirements
- [RepairThemAll Docker image](https://github.com/program-repair/RepairThemAll/blob/master/INSTALL.md#from-docker)
- Python >= 3.8
- [Pipenv](https://pypi.org/project/pipenv/)


### Installation
```console
1. git clone https://github.com/assuremoss/Automated-Program-Repair
2. cd Automated-Program-Repair/Anytime-Algorithm-2021/
3. pipenv shell
4. pipenv install
```
### Running tests
```console
1. cd tests/
2. pytest -s
```

### Results
The result can be found at [results.md](results.md). We keep updating the results as more experiments are running.
Link to raw data [Google Drive](https://drive.google.com/drive/folders/1fFg3B-DkeX-wbkl1H4HYacGxWNFGLRxR?usp=sharing)
