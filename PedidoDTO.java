package com.smartbr.clinica.model.dto;

import com.smartbr.clinica.model.dto.system.AbstractDTO;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(callSuper = false)
public class PedidoDTO extends AbstractDTO<Integer> {

	@ApiModelProperty(notes = "${campo.PedidoDTO.id.description}")
	private Integer id;

	@ApiModelProperty(notes = "${campo.PedidoDTO.descricao.description}")
	private String descricao;

	@ApiModelProperty(notes = "${campo.PedidoDTO.usuario.description}")
	private UsuarioDTO usuario;

	@ApiModelProperty(notes = "${campo.PedidoDTO.valor.description}")
	private BigDecimal valor;

	@ApiModelProperty(notes = "${campo.PedidoDTO.dataAlteracao.description}")
	private Date dataAlteracao;

	@ApiModelProperty(notes = "${campo.PedidoDTO.dataCadastro.description}")
	private Date dataCadastro;

	@ApiModelProperty(notes = "${campo.PedidoDTO.ativo.description}")
	private Boolean ativo;



}
