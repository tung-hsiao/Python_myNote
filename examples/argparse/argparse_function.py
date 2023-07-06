
def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='demo')
    parser.add_argument('--display', dest='display', help='Display online tracker output (slow) [False]',action='store_true')
    parser.add_argument("--iou_threshold", help="Minimum IOU for match.", type=float, default=0.3)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
  args = parse_args()
  display = args.display
  iou_threshold = args.iou_threshold
