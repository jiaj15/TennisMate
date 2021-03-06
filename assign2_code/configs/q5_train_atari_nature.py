class config():
    # env config
    render_train     = False
    render_test      = False
    env_name         = "Pong-v0"
    overwrite_render = True
    record           = True
    high             = 255.
    shape            = (80, 80, 1)

    # output config
    output_path  = "results/q5_train_atari_nature/"
    model_output = output_path + "model.weights/"
    log_path     = output_path + "log.txt"
    plot_output  = output_path + "scores.png"
    record_path  = output_path + "monitor/"

    checkpoint_path = output_path + "checkpoints/"
    checkpoint_freq = 250000

    # model and training config
    num_episodes_test = 50
    grad_clip         = True
    clip_val          = 10
    saving_freq       = 250000
    log_freq          = 50
    eval_freq         = 250000
    record_freq       = 250000
    soft_epsilon      = 0.05

    # nature paper hyper params
    nsteps_train       = 5000000
    batch_size         = 32
    buffer_size        = 1000000
    target_update_freq = 10000
    gamma              = 0.99
    learning_freq      = 4
    state_history      = 4
    skip_frame         = 4
    lr_begin           = 0.00025
    lr_end             = 0.00005
    lr_nsteps          = nsteps_train/2
    eps_begin          = 1.0
    eps_end            = 0.1
    eps_nsteps         = 1000000    
    learning_start     = 50000

    


    checkpoint_interval = [[-24.0, -16.0],[-16.0, -8.0],[-8.0, -4.0],[-4.0, -2.0],[-2.0,0.0],[0.0,2.0],[2.0,4.0],[4.0,8.0], [8.0, 10.0],[10 ,12]]


class config_short():
    # env config
    render_train     = False
    render_test      = False
    env_name         = "Pong-v0"
    overwrite_render = True
    record           = True
    high             = 255.
    shape            = (80, 80, 1)

    # output config
    output_path  = "results/q5_train_atari_nature/"
    model_output = output_path + "model.weights/"
    log_path     = output_path + "log.txt"
    plot_output  = output_path + "scores.png"
    record_path  = output_path + "monitor/"

    checkpoint_path = output_path + "checkpoints/"
    #checkpoint_freq = 250000
    checkpoint_freq = 250

    # model and training config
    num_episodes_test = 50
    grad_clip         = True
    clip_val          = 10

    # saving_freq       = 250000
    saving_freq       = 250
    eval_freq         = 250

    log_freq          = 50
    # eval_freq         = 250000
    record_freq       = 250000
    soft_epsilon      = 0.05

    # nature paper hyper params

    #nsteps_train       = 5000000
    nsteps_train       = 5000


    batch_size         = 32

    # buffer_size        = 1000000
    buffer_size        = 100

    target_update_freq = 10000
    gamma              = 0.99
    learning_freq      = 4
    state_history      = 4
    skip_frame         = 4
    lr_begin           = 0.00025
    lr_end             = 0.00005
    lr_nsteps          = nsteps_train/2
    eps_begin          = 1.0
    eps_end            = 0.1
    eps_nsteps         = 1000000
    
    #learning_start     = 50000
    learning_start     = 500

    checkpoint_interval = [[-22, -21],[-21, -20.0],[-20.0, -19.0],[-2.0,0.0],[0.0,2.0],[2.0,4.0],[4.0,8.0], [8.0, 16.0]]
