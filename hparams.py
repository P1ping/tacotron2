# import tensorflow as tf
from tfhparam import HParams
from text import symbols, type_set


def create_hparams(hparams_string=None, verbose=False):
    """Create model hyperparameters. Parse nondefault from given string."""

    hparams = HParams(
        ################################
        # Experiment Parameters        #
        ################################
        epochs=500,
        iters_per_checkpoint=1000,
        seed=1234,
        dynamic_loss_scaling=True,
        fp16_run=False,
        distributed_run=False,
        dist_backend="nccl",
        dist_url="tcp://localhost:54322",
        cudnn_enabled=True,
        cudnn_benchmark=False,
        ignore_layers=['embedding.weight'],

        ################################
        # Data Parameters             #
        ################################
        load_mel_from_disk=True,
        training_files='filelists/nvidia_train',
        validation_files='filelists/nvidia_val',
        text_cleaners=['english_cleaners'],

        ################################
        # Audio Parameters             #
        ################################
        max_wav_value=32768.0,
        sampling_rate=24000,
        filter_length=2048,
        hop_length=300,
        win_length=1200,
        n_mel_channels=80,
        mel_fmin=80.0,
        mel_fmax=7600.0,

        ################################
        # Model Parameters             #
        ################################
        n_symbols=len(symbols),
        n_types=len(type_set),
        symbols_embedding_dim=512,
        text_embedding_dim=768,

        # Encoder parameters
        encoder_kernel_size=5,
        encoder_n_convolutions=3,
        encoder_embedding_dim=512,

        # Decoder parameters
        n_frames_per_step=1,  # currently only 1 is supported
        decoder_rnn_dim=1024,
        prenet_dim=256,
        max_decoder_steps=1000,
        gate_threshold=0.5,
        p_attention_dropout=0.1,
        p_decoder_dropout=0.1,

        # Attention parameters
        attention_rnn_dim=1024,
        attention_dim=128,

        # Location Layer parameters
        attention_location_n_filters=32,
        attention_location_kernel_size=31,

        # Mel-post processing network parameters
        postnet_embedding_dim=512,
        postnet_kernel_size=5,
        postnet_n_convolutions=5,

        ################################
        # Optimization Hyperparameters #
        ################################
        use_saved_learning_rate=False,
        learning_rate=1e-3,
        weight_decay=1e-6,
        grad_clip_thresh=1.0,
        batch_size=32,
        mask_padding=True  # set model's padded outputs to padded values
    )

    if hparams_string:
        # tf.logging.info('Parsing command line hparams: %s', hparams_string)
        hparams.parse(hparams_string)

    if verbose:
        tf.logging.info('Final parsed hparams: %s', hparams.values())

    return hparams
