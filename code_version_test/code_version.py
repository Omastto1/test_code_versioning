import forloop as flp

fc = flp.flcore.ForloopClient(project_key=..., url=...)

pipe1 = fc.new_pipeline('immobilier')

pipe1.add(flp.nodes.RenameColumn(df_entry="", old_col_name="[]", new_col_name="house", new_var_name="villa"))
pipe1.add(flp.nodes.SelectColumns(df_entry="", column_names="[]", new_var_name=""))
pipe1.add(flp.nodes.ConstantColumn(df_entry="", value="2", column="", new_var_name=""))
pipe1.add(flp.nodes.Replace(df_entry="", columns="[]", match="pattern", replace_substring="None", pattern="asd", replacement="qwe", new_var_name=""))
pipe1.add(flp.nodes.StripColumn(df_entry="", column_name="[]", strip_mode="remove all", specific_characters="", new_var_name=""))
pipe1.add(flp.nodes.Search(df_entry="", columns="[]", match="pattern", pattern="", new_var_name=""))
