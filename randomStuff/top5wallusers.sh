#!/bin/bash
grep "wall" a2_messages.log | sort | uniq -c | sort -nr | head -5
