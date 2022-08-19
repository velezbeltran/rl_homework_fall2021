import os

"""
command1 = "python cs285/scripts/run_hw1.py "
command1 += "--expert_policy_file cs285/policies/experts/Ant.pkl "
command1 += "--env_name Ant-v2 --exp_name bc_ant --n_iter 1 "
command1 += "--expert_data cs285/expert_data/expert_data_Ant-v2.pkl "
command1 += "--ep_len 5000"
command1 += "--video_log_freq -1"

command2 = "python cs285/scripts/run_hw1.py "
command2 += "--expert_policy_file cs285/policies/experts/Walker2d.pkl "
command2 += "--env_name Walker2d-v2 --exp_name bc_walker --n_iter 1 "
command2 += "--expert_data cs285/expert_data/expert_data_Walker2d-v2.pkl "
command2 += "--video_log_freq -1"

# execute command1
print(command1)
os.system(command1)

print(command2)
os.system(command2)
"""

command3 = "python cs285/scripts/run_hw1.py "
command3 += "--expert_policy_file cs285/policies/experts/Ant.pkl "
command3 += "--env_name Ant-v2 --exp_name dagger_ant --n_iter 10 "
command3 += "--do_dagger "
command3 += "--expert_data cs285/expert_data/expert_data_Ant-v2.pkl "
command3 += "--ep_len 5000 "
#command3 += "--video_log_freq -1"


command4 = "python cs285/scripts/run_hw1.py "
command4 += "--expert_policy_file cs285/policies/experts/Walker2d.pkl "
command4 += "--env_name Walker2d-v2 --exp_name dagger_walker --n_iter 10 "
command4 += "--do_dagger "
command4 += "--expert_data cs285/expert_data/expert_data_Walker2d-v2.pkl "
command4 += "--video_log_freq 1"


# execte command1
print(command3)
os.system(command3)

print(command4)
os.system(command4)


