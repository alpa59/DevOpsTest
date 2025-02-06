#!/bin/bash
echo "Running tests..."

# Simple test to check if 1 + 1 equals 2
if [ $((1 + 1)) -eq 2 ]; then
  echo "Test passed: 1 + 1 equals 2"
else
  echo "Test failed: 1 + 1 does not equal 2"
  exit 1
fi

# Exit with success status
exit 0
