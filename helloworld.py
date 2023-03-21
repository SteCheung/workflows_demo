name: Hello Test Python Versions

on: push

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  hello-test-python-versions:
    strategy:
      matrix:
        python-version: ['3.6', '3.7', '3.8']
    runs-on: ubuntu-20.04
    steps:
    
      # Runs a single command using the runners shell, using run:
      - run: echo "Job automatically triggered by event ${{ github.event_name }}."
      
      # Runs a set of commands using the runners shell, using run: |
      - run: |
          echo "Job running on a ${{ runner.os }} server hosted by GitHub."
          echo "On branch ${{ github.ref }} of repository ${{ github.repository }}."
          
      - name: Check out repository code so it can be run by GitHub
        uses: actions/checkout@v2
        
      - run: echo "The ${{ github.repository }} repository has been cloned to the runner."
      
      - name: List files in repository
        run: |
          echo "The contents of the repository are:"
          ls ${{ github.workspace }}

      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: ${{ matrix.python-version }}
          
      - run: echo "Python has been set up."
       
      - name: Run the Python code in helloworld.py
        run: |
          echo "Running Python code"
          python helloworld.py  
