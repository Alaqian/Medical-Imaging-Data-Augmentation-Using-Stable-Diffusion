import os

MODELS = {
    "v1-4": {
        "name": "CompVis/stable-diffusion-v-1-4-original",
        "url": "https://huggingface.co/CompVis/stable-diffusion-v-1-4-original/resolve/main/sd-v1-4-full-ema.ckpt",
        "v2": False,
        "path": "pretrained_models/sd-v1-4-full-ema.ckpt",
        
    },
    "v1-5": {
        "name": "runwayml/stable-diffusion-v1-5",
        "url": "https://huggingface.co/runwayml/stable-diffusion-v1-5/blob/main/v1-5-pruned.safetensors",
        "v2": False,
        "path": "pretrained_models/v1-5-pruned.safetensors",
    },
    "v2-base": {
        "name": "stabilityai/stable-diffusion-2-base",
        "url": "https://huggingface.co/stabilityai/stable-diffusion-2-base/resolve/main/512-base-ema.safetensors",
        "v2": True,
        "path": "pretrained_models/512-base-ema.safetensors"
        },
    "v2": {
        "name": "stabilityai/stable-diffusion-2",
        "url": "https://huggingface.co/stabilityai/stable-diffusion-2/resolve/main/768-v-ema.safetensors",
        "v2": True,
        "path": "pretrained_models/768-v-ema.safetensors",
    },
    "v2-1-base": {
        "name": "stabilityai/stable-diffusion-2-1-base",
        "url": "https://huggingface.co/stabilityai/stable-diffusion-2-1-base/resolve/main/v2-1_512-ema-pruned.safetensors",
        "v2": True,
        "path": "pretrained_models/v2-1_512-ema-pruned.safetensors",
        },
    "v2-1": {
        "name": "stabilityai/stable-diffusion-2-1",
        "url": "https://huggingface.co/stabilityai/stable-diffusion-2-1/resolve/main/v2-1_768-ema-pruned.safetensors",
        "v2": True,
        "path": "pretrained_models/v2-1_768-ema-pruned.safetensors",
    }
}