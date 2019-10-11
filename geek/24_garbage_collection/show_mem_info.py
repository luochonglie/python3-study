import core.mem_utils as mem_utils


def fun():
    a = [i for i in range(10000000)]
    mem_utils.show_mem_info('after a created')


def main():
    mem_utils.show_mem_info('initial')
    fun()
    mem_utils.show_mem_info('finished')


if __name__ == '__main__':
    main()
