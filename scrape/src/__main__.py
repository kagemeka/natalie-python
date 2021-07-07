from lib.adam import (
  Adam
)

def main():
  Adam()()


def lambda_handler(
  event,
  context,
):  
  main()


if __name__ == '__main__':
  main()