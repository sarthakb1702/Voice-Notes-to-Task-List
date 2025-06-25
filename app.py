import tkinter as tk
import speech_recognition as sr

def get_mic_index():
    # Try default mic
    try:
        with sr.Microphone() as _:
            print("✅ Default microphone available")
            return None  # None = default mic
    except:
        # Print list of available mics
        mics = sr.Microphone.list_microphone_names()
        print("⚠ Default mic not available. Please select from list below:")
        for i, name in enumerate(mics):
            print(f"{i}: {name}")
        # Ask user in terminal
        while True:
            try:
                index = int(input("Enter mic index: "))
                if 0 <= index < len(mics):
                    return index
                else:
                    print("Invalid index. Try again.")
            except ValueError:
                print("Please enter a number.")

def get_voice_input():
    recognizer = sr.Recognizer()
    try:
        if MIC_INDEX is None:
            mic = sr.Microphone()
        else:
            mic = sr.Microphone(device_index=MIC_INDEX)
        with mic as source:
            status_label.config(text="🎤 Listening...")
            window.update()
            audio = recognizer.listen(source)
        text = recognizer.recognize_google(audio)
        status_label.config(text=f"✅ Recognized: {text}")
        add_task(text)
    except sr.UnknownValueError:
        status_label.config(text="❌ Could not understand.")
    except sr.RequestError as e:
        status_label.config(text=f"❌ API error: {e}")
    except Exception as e:
        status_label.config(text=f"❌ Error: {e}")

def add_task(task_text):
    task_listbox.insert(tk.END, task_text)

def toggle_task(event):
    selection = task_listbox.curselection()
    if selection:
        index = selection[0]
        current = task_listbox.get(index)
        if current.startswith("✔️ "):
            task_listbox.delete(index)
            task_listbox.insert(index, current[2:])
        else:
            task_listbox.delete(index)
            task_listbox.insert(index, f"✔️ {current}")

# GUI setup
window = tk.Tk()
window.title("🎤 Voice To-Do List")
window.geometry("400x400")

start_button = tk.Button(window, text="Start Voice Input", command=get_voice_input, font=("Arial", 14))
start_button.pack(pady=10)

status_label = tk.Label(window, text="Press button and speak your task", font=("Arial", 10))
status_label.pack()

task_listbox = tk.Listbox(window, font=("Arial", 14))
task_listbox.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)

task_listbox.bind("<Double-1>", toggle_task)

# Select mic at startup
MIC_INDEX = get_mic_index()

window.mainloop()
