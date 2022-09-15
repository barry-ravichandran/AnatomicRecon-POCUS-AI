from torch.multiprocessing import freeze_support
from ARGUS_Needle_Experiment import train_parallel_runs

def run_experiment():
    img_dir = "../../Data_PNB/stephen_prep"
    anno_dir = "../../Data_PNB/stephen_prep"

    runs = [0,1]
    vfolds = [5, 6, 7, 8, 9]
    devices = [2,3]

    train_parallel_runs(img_dir, anno_dir, runs, vfolds, devices)

if __name__ == '__main__':
    freeze_support()
    run_experiment()