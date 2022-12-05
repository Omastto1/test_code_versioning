import forloop as flp

fc = flp.flcore.ForloopClient(project_key=..., url=...)

pipe1 = fc.new_pipeline('immobilier')

pipe1.add(flp.nodes.DropColumn(df_entry="", column_name="[]", new_var_name=""))
pipe1.add(flp.nodes.Replace(df_entry="", columns="[]", match="pattern", replace_substring="False", pattern="", replacement="", new_var_name=""))
