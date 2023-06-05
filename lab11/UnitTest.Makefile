SHELL:=/bin/bash
define backup_data
	echo "" # Empty line
	-mkdir back 2> /dev/null
	mv ./input.txt ./back/
	mv ./answers.txt ./back/
endef

define restore_data
	#Restore data
	cp ./back/input.txt ./input.txt
	cp ./back/answers.txt ./answers.txt
	echo "" # Empty line
endef


define test_input
	set -e ;\
	TEST_RESULTS=$$(make tests 2> /dev/null | grep "[0-9]*[0-9]/[0-9][0-9]*" -o ); \
	TEST_PERCENTAGE=$$((100*$$TEST_RESULTS)); \
	if [ "$(1)" == "1" ]; then \
		if [ $$TEST_PERCENTAGE  -lt 25 ]; then \
			/bin/bash -c "echo  -e '\033[31m$$TEST_RESULTS'"; \
		elif [ $$TEST_PERCENTAGE  -lt 50 ]; then \
			/bin/bash -c "echo  -e '\033[35m$$TEST_RESULTS'"; \
		elif [ $$TEST_PERCENTAGE  -lt 75 ]; then \
			/bin/bash -c "echo  -e '\033[33m$$TEST_RESULTS'"; \
		elif [ $$TEST_PERCENTAGE  -lt 100 ]; then \
			/bin/bash -c "echo  -e '\033[36m$$TEST_RESULTS'"; \
		else  \
			/bin/bash -c "echo  -e '\033[32m$$TEST_RESULTS'"; \
		fi ;\
	fi
	/bin/bash -c 'echo -n -e "\033[0m"'
endef

define prepare_input
	cp ./unittests/$(1).txt ./input.txt
	cp ./unittests/$(1).answers.txt ./answers.txt
endef

define perform_test
	$(call prepare_input,$(1))
	/bin/echo -n $(2)" input tests: "
	$(call test_input,1)
endef

define generate_answers
	echo "dummy" >  ./unittests/$(1).answers.txt
	$(call prepare_input,$(1)) &> /dev/null
	$(call test_input) &> /dev/null
	cp ./output.txt ./unittests/$(1).answers.txt
	/bin/echo "Output for "$(1)".txt tests generated."
	/bin/bash -c 'echo -n -e "\033[0m"'
endef

define merge_test
	cat ./unittests/$(1).txt >> ./input.txt
	cat ./unittests/$(1).answers.txt >> ./answers.txt
endef

.SILENT all:
	$(call backup_data)	
	
	# perform_test,INPUT_FILE_NAME_WOUT_EXTENSION,TEST_NAME
	
	$(call perform_test,small,Small)
	$(call perform_test,big,Big)
	$(call perform_test,noinput,NOInput)
	$(call perform_test,sample,Sample)
	$(call perform_test,very_big,VeryBig)

	$(call restore_data)

generate:
	$(call backup_data)

	# generate_output,INPUT_FILE_NAME_WOUT_EXTENSION
	
	$(call generate_answers,small)
	$(call generate_answers,big)
	$(call generate_answers,very_big)
	$(call generate_answers,sample)
	$(call generate_answers,noinput)
	

	$(call restore_data)

merge:
	-rm ./input.txt 2>/dev/null
	-rm ./answers.txt 2>/dev/null

	$(call merge_test,small)
	$(call merge_test,big)
	$(call merge_test,very_big)
	$(call merge_test,sample)
	$(call merge_test,noinput)
