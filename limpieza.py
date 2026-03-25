import pandas as pd


column_names = [
"duration","protocol_type","service","flag","src_bytes","dst_bytes","land","wrong_fragment","urgent",
"hot","num_failed_logins","logged_in","num_compromised","root_shell","su_attempted","num_root",
"num_file_creations","num_shells","num_access_files","num_outbound_cmds","is_host_login",
"is_guest_login","count","srv_count","serror_rate","srv_serror_rate","rerror_rate",
"srv_rerror_rate","same_srv_rate","diff_srv_rate","srv_diff_host_rate","dst_host_count",
"dst_host_srv_count","dst_host_same_srv_rate","dst_host_diff_srv_rate",
"dst_host_same_src_port_rate","dst_host_srv_diff_host_rate","dst_host_serror_rate",
"dst_host_srv_serror_rate","dst_host_rerror_rate","dst_host_srv_rerror_rate",
"label","difficulty"
]


df = pd.read_csv("data/KDDTrain+_20Percent.txt", names=column_names)


selected_columns = [
    "duration",
    "protocol_type",
    "src_bytes",
    "dst_bytes",
    "count",
    "label"
]

df = df[selected_columns]


df["protocol_type"] = df["protocol_type"].map({
    "tcp": 0,
    "udp": 1,
    "icmp": 2
})


df["label"] = df["label"].apply(lambda x: 0 if x == "normal" else 1)



df.to_csv("data/datos_limpios.csv", index=False)





conteo = df["label"].value_counts().sort_index()
porcentaje = df["label"].value_counts(normalize=True).sort_index() * 100

print("\nDistribución de datos:")
print("Total de registros", conteo[0] + conteo[1])
print(f"Normal (0): {conteo[0]} registros - {porcentaje[0]:.2f}%")
print(f"Ataque (1): {conteo[1]} registros - {porcentaje[1]:.2f}%")