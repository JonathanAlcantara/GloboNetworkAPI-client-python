# -*- coding:utf-8 -*-
'''
Title: Infrastructure NetworkAPI
Author: globo.com / TQI
Copyright: ( c )  2009 globo.com todos os direitos reservados.
'''

from networkapiclient.GenericClient import GenericClient
from networkapiclient.utils import is_valid_int_param
from networkapiclient.exception import InvalidParameterError

class Network(GenericClient):
    def __init__(self, networkapi_url, user, password, user_ldap=None):
        """Class constructor receives parameters to connect to the networkAPI.
        :param networkapi_url: URL to access the network API.
        :param user: User for authentication.
        :param password: Password for authentication.
        """
        super(Network, self).__init__(networkapi_url, user, password, user_ldap);

    def create_networks(self, ids, id_vlan):
        """Set column 'active = 1' in tables redeipv4 and redeipv6]

        :param ids: ID for NetworkIPv4 and/or NetworkIPv6

        :return: Nothing
        """

        network_map = dict()
        network_map['ids'] = ids
        network_map['id_vlan'] = id_vlan

        code, xml = self.submit({'network':network_map}, 'PUT', 'network/create/')

        return self.response(code, xml)

    def add_network(self, network, id_vlan, id_network_type, id_environment_vip=None):
        """
        Add new network

        :param network: 0 to IPv4 or 1 to IPv6
        :param id_vlan: Identifier of the Vlan. Integer value and greater than zero.
        :param id_network_type: Identifier of the NetworkType. Integer value and greater than zero.
        :param id_environment_vip: Identifier of the Environment Vip. Integer value and greater than zero.

        :return: Following dictionary:

        ::

          {'network':{'id': <id_network>,
          'rede': <network>,
          'broadcast': <broadcast> (if is IPv4),
          'mask': <net_mask>,
          'id_vlan': <id_vlan>,
          'id_tipo_rede': <id_network_type>,
          'id_ambiente_vip': <id_ambiente_vip>,
          'active': <active>} } 

        :raise TipoRedeNaoExisteError: NetworkType not found.
        :raise InvalidParameterError: Invalid ID for Vlan or NetworkType.
        :raise EnvironmentVipNotFoundError: Environment VIP not registered.
        :raise IPNaoDisponivelError: Network address unavailable to create a NetworkIPv4.
        :raise NetworkIPRangeEnvError: Other environment already have this ip range.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        network_map = dict()
        network_map['network'] = network
        network_map['id_vlan'] = id_vlan
        network_map['id_network_type'] = id_network_type
        network_map['id_environment_vip'] = id_environment_vip

        code, xml = self.submit({'network':network_map}, 'POST', 'network/add/')

        return self.response(code, xml)

    def add_network_ipv4(self, id_vlan, id_tipo_rede, id_ambiente_vip=None, prefix=None):
        """
        Add new networkipv4

        :param id_vlan: Identifier of the Vlan. Integer value and greater than zero.
        :param id_tipo_rede: Identifier of the NetworkType. Integer value and greater than zero.
        :param id_ambiente_vip: Identifier of the Environment Vip. Integer value and greater than zero.
        :param prefix: Prefix.

        :return: Following dictionary:

        ::

          {'vlan': {'id': < id_vlan >,
          'nome': < nome_vlan >,
          'num_vlan': < num_vlan >,
          'id_tipo_rede': < id_tipo_rede >,
          'id_ambiente': < id_ambiente >,
          'rede_oct1': < rede_oct1 >,
          'rede_oct2': < rede_oct2 >,
          'rede_oct3': < rede_oct3 >,
          'rede_oct4': < rede_oct4 >,
          'bloco': < bloco >,
          'mascara_oct1': < mascara_oct1 >,
          'mascara_oct2': < mascara_oct2 >,
          'mascara_oct3': < mascara_oct3 >,
          'mascara_oct4': < mascara_oct4 >,
          'broadcast': < broadcast >,
          'descricao': < descricao >,
          'acl_file_name': < acl_file_name >,
          'acl_valida': < acl_valida >,
          'ativada': < ativada >}} 

        :raise TipoRedeNaoExisteError: NetworkType not found.
        :raise InvalidParameterError: Invalid ID for Vlan or NetworkType.
        :raise EnvironmentVipNotFoundError: Environment VIP not registered.
        :raise IPNaoDisponivelError: Network address unavailable to create a NetworkIPv4.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        vlan_map = dict()
        vlan_map['id_vlan'] = id_vlan
        vlan_map['id_tipo_rede'] = id_tipo_rede
        vlan_map['id_ambiente_vip'] = id_ambiente_vip
        vlan_map['prefix'] = prefix

        code, xml = self.submit({'vlan':vlan_map}, 'POST', 'network/ipv4/add/')

        return self.response(code, xml)

    def add_network_ipv4_hosts(self, id_vlan, id_tipo_rede, num_hosts, id_ambiente_vip=None):
        """
        Add new networkipv4

        :param id_vlan: Identifier of the Vlan. Integer value and greater than zero.
        :param id_tipo_rede: Identifier of the NetworkType. Integer value and greater than zero.
        :param num_hosts: Number of hosts expected. Integer value and greater than zero.
        :param id_ambiente_vip: Identifier of the Environment Vip. Integer value and greater than zero.

        :return: Following dictionary:

        ::

          {'vlan': {'id': < id_vlan >,
          'nome': < nome_vlan >,
          'num_vlan': < num_vlan >,
          'id_tipo_rede': < id_tipo_rede >,
          'id_ambiente': < id_ambiente >,
          'rede_oct1': < rede_oct1 >,
          'rede_oct2': < rede_oct2 >,
          'rede_oct3': < rede_oct3 >,
          'rede_oct4': < rede_oct4 >,
          'bloco': < bloco >,
          'mascara_oct1': < mascara_oct1 >,
          'mascara_oct2': < mascara_oct2 >,
          'mascara_oct3': < mascara_oct3 >,
          'mascara_oct4': < mascara_oct4 >,
          'broadcast': < broadcast >,
          'descricao': < descricao >,
          'acl_file_name': < acl_file_name >,
          'acl_valida': < acl_valida >,
          'ativada': < ativada >}} 

        :raise TipoRedeNaoExisteError: NetworkType not found.
        :raise InvalidParameterError: Invalid ID for Vlan or NetworkType.
        :raise EnvironmentVipNotFoundError: Environment VIP not registered.
        :raise IPNaoDisponivelError: Network address unavailable to create a NetworkIPv4.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        vlan_map = dict()
        vlan_map['id_vlan'] = id_vlan
        vlan_map['id_tipo_rede'] = id_tipo_rede
        vlan_map['num_hosts'] = num_hosts
        vlan_map['id_ambiente_vip'] = id_ambiente_vip

        code, xml = self.submit({'vlan': vlan_map}, 'PUT', 'network/ipv4/add/')

        return self.response(code, xml)

    def edit_network(self, id_network, ip_type , id_net_type, id_env_vip=None):
        """
        Edit a network 4 or 6

        :param id_network: Identifier of the Network. Integer value and greater than zero.
        :param id_net_type: Identifier of the NetworkType. Integer value and greater than zero.
        :param id_env_vip: Identifier of the Environment Vip. Integer value and greater than zero.
        :param ip_type: Identifier of the Network IP Type: 0 = IP4 Network; 1 = IP6 Network;

        :return: None

        :raise TipoRedeNaoExisteError: NetworkType not found.
        :raise InvalidParameterError: Invalid ID for Vlan or NetworkType.
        :raise EnvironmentVipNotFoundError: Environment VIP not registered.
        :raise IPNaoDisponivelError: Network address unavailable to create a NetworkIPv4.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        net_map = dict()
        net_map['id_network'] = id_network
        net_map['ip_type'] = ip_type
        net_map['id_net_type'] = id_net_type
        net_map['id_env_vip'] = id_env_vip

        code, xml = self.submit({'net':net_map}, 'POST', 'network/edit/')

        return self.response(code, xml)

    def get_network_ipv4(self, id_network):
        """
        Get networkipv4

        :param id_network: Identifier of the Network. Integer value and greater than zero.
        :return: Following dictionary:

        ::

          {'network': {'id': < id_networkIpv6 >,
          'network_type': < id_tipo_rede >,
          'ambiente_vip': < id_ambiente_vip >,
          'vlan': <id_vlan>
          'oct1': < rede_oct1 >,
          'oct2': < rede_oct2 >,
          'oct3': < rede_oct3 >,
          'oct4': < rede_oct4 >
          'blocK': < bloco >,
          'mask_oct1': < mascara_oct1 >,
          'mask_oct2': < mascara_oct2 >,
          'mask_oct3': < mascara_oct3 >,
          'mask_oct4': < mascara_oct4 >,
          'active': < ativada >,
          'broadcast':<'broadcast>, }}  

        :raise NetworkIPv4NotFoundError: NetworkIPV4 not found.
        :raise InvalidValueError: Invalid ID for NetworkIpv4
        :raise NetworkIPv4Error: Error in NetworkIpv4
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_network):
            raise InvalidParameterError(u'O id do rede ip4 foi informado incorretamente.')

        url = 'network/ipv4/id/' + str(id_network) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def get_network_ipv6(self, id_network):
        """
        Get networkipv6

        :param id_network: Identifier of the Network. Integer value and greater than zero.
        :return: Following dictionary:

        ::

          {'network': {'id': < id_networkIpv6 >,
          'network_type': < id_tipo_rede >,
          'ambiente_vip': < id_ambiente_viṕ >,
          'vlan': <id_vlan>
          'block1': < rede_oct1 >,
          'block2': < rede_oct2 >,
          'block3': < rede_oct3 >,
          'block4': < rede_oct4 >,
          'block5': < rede_oct4 >,
          'block6': < rede_oct4 >,
          'block7': < rede_oct4 >,
          'block8': < rede_oct4 >,
          'blocK': < bloco >,
          'mask1': < mascara_oct1 >,
          'mask2': < mascara_oct2 >,
          'mask3': < mascara_oct3 >,
          'mask4': < mascara_oct4 >,
          'mask5': < mascara_oct4 >,
          'mask6': < mascara_oct4 >,
          'mask7': < mascara_oct4 >,
          'mask8': < mascara_oct4 >,
          'active': < ativada >, }} 

        :raise NetworkIPv6NotFoundError: NetworkIPV6 not found.
        :raise InvalidValueError: Invalid ID for NetworkIpv6
        :raise NetworkIPv6Error: Error in NetworkIpv6
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_network):
            raise InvalidParameterError(u'O id do rede ip6 foi informado incorretamente.')


        url = 'network/ipv6/id/' + str(id_network) + '/'

        code, xml = self.submit(None, 'GET', url)

        return self.response(code, xml)

    def deallocate_network_ipv4(self, id_network_ipv4):
        """
        Deallocate all relationships between NetworkIPv4.

        :param id_network_ipv4: ID for NetworkIPv4

        :return: Nothing

        :raise InvalidParameterError: Invalid ID for NetworkIPv4.
        :raise NetworkIPv4NotFoundError: NetworkIPv4 not found.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_network_ipv4):
            raise InvalidParameterError(u'The identifier of NetworkIPv4 is invalid or was not informed.')

        url = 'network/ipv4/' + str(id_network_ipv4) + '/deallocate/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)

    def add_network_ipv6(self, id_vlan, id_tipo_rede, id_ambiente_vip=None, prefix=None):
        """
        Add new networkipv6

        :param id_vlan: Identifier of the Vlan. Integer value and greater than zero.
        :param id_tipo_rede: Identifier of the NetworkType. Integer value and greater than zero.
        :param id_ambiente_vip: Identifier of the Environment Vip. Integer value and greater than zero.
        :param prefix: Prefix.

        :return: Following dictionary:

        ::

          {'vlan': {'id': < id_vlan >,
          'nome': < nome_vlan >,
          'num_vlan': < num_vlan >,
          'id_tipo_rede': < id_tipo_rede >,
          'id_ambiente': < id_ambiente >,
          'rede_oct1': < rede_oct1 >,
          'rede_oct2': < rede_oct2 >,
          'rede_oct3': < rede_oct3 >,
          'rede_oct4': < rede_oct4 >,
          'rede_oct5': < rede_oct4 >,
          'rede_oct6': < rede_oct4 >,
          'rede_oct7': < rede_oct4 >,
          'rede_oct8': < rede_oct4 >,
          'bloco': < bloco >,
          'mascara_oct1': < mascara_oct1 >,
          'mascara_oct2': < mascara_oct2 >,
          'mascara_oct3': < mascara_oct3 >,
          'mascara_oct4': < mascara_oct4 >,
          'mascara_oct5': < mascara_oct4 >,
          'mascara_oct6': < mascara_oct4 >,
          'mascara_oct7': < mascara_oct4 >,
          'mascara_oct8': < mascara_oct4 >,
          'broadcast': < broadcast >,
          'descricao': < descricao >,
          'acl_file_name': < acl_file_name >,
          'acl_valida': < acl_valida >,
          'ativada': < ativada >}} 

        :raise TipoRedeNaoExisteError: NetworkType not found.
        :raise InvalidParameterError: Invalid ID for Vlan or NetworkType.
        :raise EnvironmentVipNotFoundError: Environment VIP not registered.
        :raise IPNaoDisponivelError: Network address unavailable to create a NetworkIPv6.
        :raise ConfigEnvironmentInvalidError: Invalid Environment Configuration or not registered
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        vlan_map = dict()
        vlan_map['id_vlan'] = id_vlan
        vlan_map['id_tipo_rede'] = id_tipo_rede
        vlan_map['id_ambiente_vip'] = id_ambiente_vip
        vlan_map['prefix'] = prefix

        code, xml = self.submit({'vlan':vlan_map}, 'POST', 'network/ipv6/add/')

        return self.response(code, xml)

    def add_network_ipv6_hosts(self, id_vlan, id_tipo_rede, num_hosts, id_ambiente_vip=None):
        """
        Add new networkipv6

        :param id_vlan: Identifier of the Vlan. Integer value and greater than zero.
        :param id_tipo_rede: Identifier of the NetworkType. Integer value and greater than zero.
        :param num_hosts: Number of hosts expected. Integer value and greater than zero.
        :param id_ambiente_vip: Identifier of the Environment Vip. Integer value and greater than zero.

        :return: Following dictionary:

        ::

          {'vlan': {'id': < id_vlan >,
          'nome': < nome_vlan >,
          'num_vlan': < num_vlan >,
          'id_tipo_rede': < id_tipo_rede >,
          'id_ambiente': < id_ambiente >,
          'rede_oct1': < rede_oct1 >,
          'rede_oct2': < rede_oct2 >,
          'rede_oct3': < rede_oct3 >,
          'rede_oct4': < rede_oct4 >,
          'rede_oct5': < rede_oct4 >,
          'rede_oct6': < rede_oct4 >,
          'rede_oct7': < rede_oct4 >,
          'rede_oct8': < rede_oct4 >,
          'bloco': < bloco >,
          'mascara_oct1': < mascara_oct1 >,
          'mascara_oct2': < mascara_oct2 >,
          'mascara_oct3': < mascara_oct3 >,
          'mascara_oct4': < mascara_oct4 >,
          'mascara_oct5': < mascara_oct4 >,
          'mascara_oct6': < mascara_oct4 >,
          'mascara_oct7': < mascara_oct4 >,
          'mascara_oct8': < mascara_oct4 >,
          'broadcast': < broadcast >,
          'descricao': < descricao >,
          'acl_file_name': < acl_file_name >,
          'acl_valida': < acl_valida >,
          'ativada': < ativada >}} 

        :raise TipoRedeNaoExisteError: NetworkType not found.
        :raise InvalidParameterError: Invalid ID for Vlan or NetworkType.
        :raise EnvironmentVipNotFoundError: Environment VIP not registered.
        :raise IPNaoDisponivelError: Network address unavailable to create a NetworkIPv6.
        :raise ConfigEnvironmentInvalidError: Invalid Environment Configuration or not registered
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """
        vlan_map = dict()
        vlan_map['id_vlan'] = id_vlan
        vlan_map['id_tipo_rede'] = id_tipo_rede
        vlan_map['num_hosts'] = num_hosts
        vlan_map['id_ambiente_vip'] = id_ambiente_vip

        code, xml = self.submit({'vlan':vlan_map}, 'PUT', 'network/ipv6/add/')

        return self.response(code, xml)

    def deallocate_network_ipv6(self, id_network_ipv6):
        """
        Deallocate all relationships between NetworkIPv6.

        :param id_network_ipv6: ID for NetworkIPv6

        :return: Nothing

        :raise InvalidParameterError: Invalid ID for NetworkIPv6.
        :raise NetworkIPv6NotFoundError: NetworkIPv6 not found.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        if not is_valid_int_param(id_network_ipv6):
            raise InvalidParameterError(u'The identifier of NetworkIPv6 is invalid or was not informed.')

        url = 'network/ipv6/' + str(id_network_ipv6) + '/deallocate/'

        code, xml = self.submit(None, 'DELETE', url)

        return self.response(code, xml)

    def remove_networks(self, ids):
        """
        Set column 'active = 0' in tables redeipv4 and redeipv6]

        :param ids: ID for NetworkIPv4 and/or NetworkIPv6

        :return: Nothing

        :raise NetworkInactiveError: Unable to remove the network because it is inactive.
        :raise InvalidParameterError: Invalid ID for Network or NetworkType.
        :raise NetworkIPv4NotFoundError: NetworkIPv4 not found.
        :raise NetworkIPv6NotFoundError: NetworkIPv6 not found.
        :raise DataBaseError: Networkapi failed to access the database.
        :raise XMLError: Networkapi failed to generate the XML response.
        """

        network_map = dict()
        network_map['ids'] = ids

        code, xml = self.submit({'network':network_map}, 'PUT', 'network/remove/')

        return self.response(code, xml)


