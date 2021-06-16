import numpy as np
import sqlite3
from Node import *

def main():
    conn = sqlite3.connect("OurLogistics.db");
    cs = conn.cursor();
    cs.execute("""
    select * from Containers;
    """);
    containers = [Container(containerId, location, loaded, destination)
                  for containerId, location, loaded, destination
                  in cs.fetchall()];
    cs.close();
    conn.close();

main();
