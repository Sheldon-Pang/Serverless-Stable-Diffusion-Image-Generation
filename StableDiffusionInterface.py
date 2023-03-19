import tkinter as tk
import base64
from PIL import Image
from io import BytesIO
import banana_dev as banana


def save_image(image_data):
    image_encoded = image_data.encode('utf-8')
    image_bytes = BytesIO(base64.b64decode(image_encoded))
    image = Image.open(image_bytes)
    image.save("output.jpg")


def run_model():
    model_inputs = {
        "endpoint": "txt2img",
        "params": {
            "prompt": entry_prompt.get(),
            "negative_prompt": entry_negative_prompt.get(),
            "steps": int(entry_steps.get()),
            "sampler_name": entry_sampler_name.get(),
            "cfg_scale": float(entry_cfg_scale.get()),
            "seed": int(entry_seed.get()),
            "batch_size": int(entry_batch_size.get()),
            "n_iter": int(entry_n_iter.get()),
            "width": int(entry_width.get()),
            "height": int(entry_height.get()),
            "tiling": False
        }
    }

    # Change this to you key
    api_key = "Your API KEY"
    model_key = "Your Model Key"

    out = banana.run(api_key, model_key, model_inputs)
    print(out)
    save_image(out["modelOutputs"][0]["images"][0])


root = tk.Tk()
root.title("Banana Dev - Image Generator")

entry_prompt = tk.Entry(root)
entry_prompt.insert(0, "an astronaut riding a (horse:motorcycle:0.5) on the moon")
entry_negative_prompt = tk.Entry(root)
entry_negative_prompt.insert(0, "cartoonish, low quality")
entry_steps = tk.Entry(root)
entry_steps.insert(0, "25")
entry_sampler_name = tk.Entry(root)
entry_sampler_name.insert(0, "Euler a")
entry_cfg_scale = tk.Entry(root)
entry_cfg_scale.insert(0, "7.5")
entry_seed = tk.Entry(root)
entry_seed.insert(0, "42")
entry_batch_size = tk.Entry(root)
entry_batch_size.insert(0, "1")
entry_n_iter = tk.Entry(root)
entry_n_iter.insert(0, "1")
entry_width = tk.Entry(root)
entry_width.insert(0, "768")
entry_height = tk.Entry(root)
entry_height.insert(0, "768")

entry_prompt.grid(row=0, column=1)
entry_negative_prompt.grid(row=1, column=1)
entry_steps.grid(row=2, column=1)
entry_sampler_name.grid(row=3, column=1)
entry_cfg_scale.grid(row=4, column=1)
entry_seed.grid(row=5, column=1)
entry_batch_size.grid(row=6, column=1)
entry_n_iter.grid(row=7, column=1)
entry_width.grid(row=8, column=1)
entry_height.grid(row=9, column=1)

label_prompt = tk.Label(root, text="Prompt")
label_negative_prompt = tk.Label(root, text="Negative Prompt")
label_steps = tk.Label(root, text="Steps")
label_sampler_name = tk.Label(root, text="Sampler Name")
label_cfg_scale = tk.Label(root, text="CFG Scale")
label_seed = tk.Label(root, text="Seed")
label_batch_size = tk.Label(root, text="Batch Size")
label_n_iter = tk.Label(root, text="N Iter")
label_width = tk.Label(root, text="Width")
label_height = tk.Label(root, text="Height")

label_prompt.grid(row=0, column=0)
label_negative_prompt.grid(row=1, column=0)
label_steps.grid(row=2, column=0)
label_sampler_name.grid(row=3, column=0)
label_cfg_scale.grid(row=4, column=0)
label_seed.grid(row=5, column=0)
label_batch_size.grid(row=6, column=0)
label_n_iter.grid(row=7, column=0)
label_width.grid(row=8, column=0)
label_height.grid(row=9, column=0)

generate_button = tk.Button(root, text="Generate Image", command=run_model)
generate_button.grid(row=10, columnspan=2)

root.mainloop()
